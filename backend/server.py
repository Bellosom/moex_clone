import aiomysql


from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from data import user, password, db_name, host

# Глобальный флаг для ограничения доступа
is_restricted = False

def set_restricted(value: bool):
    global is_restricted
    is_restricted = value

def get_restricted():
    return is_restricted

app = FastAPI()

# CORS settings
origins = [
    'http://localhost:3000',
    'http://openinterest.ru',
    'http://www.openinterest.ru',
    'http://77.222.38.185',
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def check_restriction(request: Request, call_next):
    if get_restricted():
        raise HTTPException(status_code=503, detail="Сервер недоступен с 02:30 до 03:00")
    response = await call_next(request)
    return response

class ChartData(BaseModel):
    dates: List[str]
    values: List[float]
    values2: Optional[List[float]] = None
    label: str

async def fetch_data_from_db(futureCode: str, query: str):
    print(password)
    connection = None
    try:
        connection = await aiomysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            autocommit=True
        )
        async with connection.cursor(aiomysql.DictCursor) as cursor:
            start_time = datetime.now()
            await cursor.execute(query, (futureCode,))
            result = await cursor.fetchall()
            end_time = datetime.now()
            print(f"Query execution time: {end_time - start_time}")
    except Exception as e:
        print(f"Error occurred: {e}")
        raise
    finally:
        if connection:
            connection.close()
    return result

@app.get("/api/get_chart_data", response_model=ChartData)
async def get_chart_data(futureCode: str, chartNumber: int):
    column = ""
    column2 = None
    if chartNumber == 1:
        column = "JuridicalLong1 - JuridicalShort1"
    elif chartNumber == 2:
        column = "JuridicalLong1 + JuridicalShort1"
    elif chartNumber == 3:
        column = "JuridicalLong3 - JuridicalShort3"
    elif chartNumber == 4:
        column = "JuridicalLong1"
        column2 = "JuridicalShort1"
    elif chartNumber == 5:
        column = "PhysicalLong1 - PhysicalShort1"
    elif chartNumber == 6:
        column = "PhysicalLong1 + PhysicalShort1"
    elif chartNumber == 7:
        column = "PhysicalLong3 - PhysicalShort3"
    elif chartNumber == 8:
        column = "PhysicalLong1"
        column2 = "PhysicalShort1"

    if column2:
        query = f"""
        SELECT date, {column} AS value1, {column2} AS value2
        FROM xml_data
        WHERE fve = %s
        ORDER BY date;
        """
    else:
        query = f"""
        SELECT date, {column} AS value
        FROM xml_data
        WHERE fve = %s
        ORDER BY date;
        """

    try:
        result = await fetch_data_from_db(futureCode, query)

        if not result:
            raise HTTPException(status_code=404, detail="Data not found")

        dates = [row['date'].strftime('%Y-%m-%d') for row in result]
        values1 = [row['value1'] if column2 else row['value'] for row in result]
        values2 = [row['value2'] for row in result] if column2 else None

        return {
            "dates": dates,
            "values": values1,
            "values2": values2,
            "label": f"Chart {chartNumber} for {futureCode}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def create_server():
    return app