import json

import os


def find_operations_json(name_json='operations.json'):
    """ Ищет путь к operations.json"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    operations_json_path = os.path.join(script_dir, name_json)
    if os.path.exists(operations_json_path):
        return operations_json_path
    else:
        return False


def import_json():
    """ Открывает json объект и возвращает его"""
    with open(find_operations_json(), 'r', encoding='utf-8') as file:
        return json.load(file)


def executed(operation):
    """ Функция для сортировки по bool"""
    return operation.get('state') == 'EXECUTED'


def filter_executed():
    """ Фильтрация import_json по EXECUTED()"""
    sorted_operations = import_json()
    return filter(executed, sorted_operations)


def sorted_date():
    """ Сортировка отфильтрованного списка по убыванию дат"""
    json_data = list(filter_executed())
    filtered_data = [i for i in json_data if 'date' in i]
    return sorted(filtered_data, key=lambda x: x['date'], reverse=True)