import re
import os
import xml.etree.ElementTree as ET


from bs4 import BeautifulSoup
from data import first_url, second_url, scraper


def get_all_tovars(url=first_url):
    '''Получаем все коды контрактов фьючеров'''
    response = scraper.get(url=url, timeout=180)
    soup = BeautifulSoup(response.text, 'html.parser')
    table_info = soup.find('div', class_='FortsMainWUC')
    table_rows = table_info.find_all('table', class_='table1 listMainFortsIssue')

    row_info = []
    for rows in table_rows:
        links = rows.find_all('a')
        for link in links:
            row_name = re.sub(r'-.*', '', link.text.strip())
            row_info.append(row_name)

    return row_info


def clean_data(data: str):
    '''Удаляет неразрывные пробелы и третий элемент из данных'''
    if isinstance(data, dict):
        return {key: clean_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        if len(data) >= 3:
            del data[2]  # Удаляем третий элемент
        return [clean_data(item) for item in data]
    elif isinstance(data, str):
        return data.replace('\xa0', ' ')  # Заменяем \xa0 на обычный пробел
    return data


def json_to_xml(json_obj):
    """Преобразует JSON в XML."""
    elem = ET.Element("root")

    def build_xml(element, json_obj):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                sub_elem = ET.SubElement(element, key)
                build_xml(sub_elem, value)
        elif isinstance(json_obj, list):
            for item in json_obj:
                sub_elem = ET.SubElement(element, "item")
                build_xml(sub_elem, item)
        else:
            element.text = str(json_obj)

    build_xml(elem, json_obj)
    return ET.tostring(elem, encoding='unicode')


def save_to_xml(folder_path, param, date, data):
    '''Сохраняет данные в XML файл'''
    xml_result = json_to_xml(data)
    file_path = os.path.join(folder_path, f'{param}_{date}.xml')
    
    with open(file_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_result)


def get_open_positions(params_url, date):
    '''Вся информация по открытым позициям'''

    folder_path1 = 'xml_data_all_dates'
    os.makedirs(folder_path1, exist_ok=True)

    folder_path = os.path.join(folder_path1, f'xml_data_{date}')
    os.makedirs(folder_path, exist_ok=True)

    for param in params_url:
        response = scraper.get(fr'{second_url}{date}/F/{param}/json', timeout=180)
        response.encoding = 'utf-8'
        data = response.json()

        if data and data != []:
            cleaned_data = clean_data(data)
            save_to_xml(folder_path, param, date, cleaned_data)