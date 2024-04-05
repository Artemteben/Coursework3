import datetime


class PrintHistory:
    """ Принимает json-объект и его индекс, тянет словарь"""

    def __init__(self, dict_json_all, number_operation):
        self.number_operation = number_operation
        self.dict_json_all = dict_json_all
        self.dict_json = list(self.dict_json_all)[self.number_operation]
    def date_print(self):
        """ Запрос у словаря строки по ключу 'date',
        форматирует строку и возвращет дату в формате '%d.%m.%Y'"""

        date_slice = self.dict_json.get('date')
        date_print_datetime = datetime.datetime.strptime(date_slice[:10], "%Y-%m-%d")
        date_print_point = date_print_datetime.strftime("%d.%m.%Y")
        return date_print_point

    def print_line(self, line_title):
        """ Запрашивает у словаря по ключу строку и возвращает её значение"""

        line_output = self.dict_json.get(line_title, "Нет значения ключа/самого ключа")
        return line_output

    def account_code(self, from_and_to):
        """ Зашифровка карт  в формате  XXXX XX** **** XXXX
        счета в формате  **XXXX"""

        payment = self.dict_json.get(from_and_to, "NONE********NONE")
        if "Счет" in payment:
            return f'Счет **{payment[-4:]}'
        else:
            return f'{payment[-16:-12]} {payment[-12:-10]}** **** {payment[-4:]}'

    def currency(self):
        """ Выводит значение словаря operationAmount возвращает значение amount и name"""
        operation_amount = self.dict_json.get("operationAmount")
        currency = operation_amount.get("currency")
        return operation_amount.get("amount") + ' ' + currency.get("name")