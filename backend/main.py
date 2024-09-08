import pytz
import uvicorn
import asyncio


from datetime import datetime, time as dt_time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from server import create_server, set_restricted, get_restricted
from parser import get_all_tovars, get_open_positions
from from_xml_to_db import parse_xml_and_insert


# Создаем сервер
app = create_server()

# Планировщик задач
scheduler = AsyncIOScheduler()

async def scheduled_task():
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    date = now.strftime(r"%d.%m.%Y")
    print(f'Парсинг открытых позиций за {date}')
    await asyncio.to_thread(get_open_positions, params_url=get_all_tovars(), date=date)  # Асинхронное выполнение парсера
    await asyncio.to_thread(parse_xml_and_insert, date=date)

async def restrict_access():
    while True:
        current_time = datetime.now(pytz.timezone('Europe/Moscow')).time()
        if dt_time(2, 30) <= current_time < dt_time(3, 0):
            if not get_restricted():
                set_restricted(True)
                print("Сервер недоступен с 02:30 до 03:00")
                await scheduled_task()  # Выполняем задачу парсинга
        else:
            if get_restricted():
                set_restricted(False)
                print("Сервер снова доступен")
        await asyncio.sleep(60)  # Проверяем каждые 60 секунд

async def main():
    # Запускаем задачу для ограничения доступа
    asyncio.create_task(restrict_access())

    # Запускаем FastAPI приложение
    config = uvicorn.Config(app, host='0.0.0.0', port=8000)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())