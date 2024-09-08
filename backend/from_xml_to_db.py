import os
import pymysql
import xml.etree.ElementTree as ET


from data import folder_path, host, db_name, user, password
from datetime import datetime


def parse_xml_and_insert(folder_path=folder_path, date=None):
    '''Функция для парсинга XML и вставки данных в базу'''

    # Настройка подключения к базе данных
    connection = pymysql.connect(
        host=host,
        user=user,
        port=3306,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()

    for folder_name in os.listdir(folder_path):
        if folder_name == f'xml_data_{date}':
            date_zero = folder_name.split('_')[2]
            date_zero = datetime.strptime(date_zero, '%d.%m.%Y').strftime('%Y-%m-%d')
            folder_path_full = os.path.join(folder_path, folder_name)

            # Проход по всем XML файлам в папке
            try_category = []
            for xml_file in os.listdir(folder_path_full):
                category = xml_file.split('_')[0]
                if xml_file.endswith('.xml'):
                    file_path = os.path.join(folder_path_full, xml_file)

                    # Парсинг XML файла
                    tree = ET.parse(file_path)
                    root = tree.getroot()

                    try:
                        item = root.findall('item')

                        JuridicalLong1 = item[0].find('JuridicalLong').text.replace(' ', '')
                        JuridicalLong3 = item[2].find('JuridicalLong').text.replace(' ', '')
                        JuridicalShort1 = item[0].find('JuridicalShort').text.replace(' ', '')
                        JuridicalShort3 = item[2].find('JuridicalShort').text.replace(' ', '')

                        PhysicalLong1 = item[0].find('PhysicalLong').text.replace(' ', '')
                        PhysicalLong3 = item[2].find('PhysicalLong').text.replace(' ', '')
                        PhysicalShort1 = item[0].find('PhysicalShort').text.replace(' ', '')
                        PhysicalShort3 = item[2].find('PhysicalShort').text.replace(' ', '')

                        try_category.append(category)

                        # Проверка на наличие записи в базе данных
                        check_query = """
                            SELECT COUNT(*) as count FROM xml_data WHERE fve = %s AND date = %s;
                        """
                        cursor.execute(check_query, (category, date_zero))
                        result = cursor.fetchone()

                        if result['count'] == 0:
                            # Вставка данных только если запись отсутствует
                            insert_query = """
                                INSERT INTO xml_data (fve, date, JuridicalLong1, JuridicalShort1, JuridicalLong3, JuridicalShort3,
                                                      PhysicalLong1, PhysicalLong3, PhysicalShort1, PhysicalShort3)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            """

                            cursor.execute(insert_query, (category, date_zero,
                                                          int(JuridicalLong1), int(JuridicalShort1),
                                                          int(JuridicalLong3), int(JuridicalShort3),
                                                          int(PhysicalLong1), int(PhysicalLong3),
                                                          int(PhysicalShort1), int(PhysicalShort3)))

                            connection.commit()

                            print(f'Inserted data from {xml_file}')
                        else:
                            print(f'Record for {category} on {date_zero} already exists, skipping.')

                    except Exception as e:
                        print(f'{xml_file}: {e}')


    connection.commit()
    cursor.close()
    connection.close()