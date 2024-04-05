from utlis.class_print_history import PrintHistory


def test_print_history_date():
    dict_test = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"},
                 {"id": 41428829, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                  "to": "Счет 35383033474447895560"}]

    assert PrintHistory(dict_test, 0).date_print() == '26.08.2019'


def test_print_history_line():
    dict_test = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"},
                 {"id": 41428829, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "description": "Перевод организации", "from": "MasterCard 7158300734726758",
                  "to": "Счет 35383033474447895560"}]
    copy = PrintHistory(dict_test, 0)
    assert copy.print_line('id') == 441945886
    assert copy.print_line('test') == "Нет значения ключа или самого ключа"


def test_print_history_account_code():
    dict_test = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"},
                 {"id": 41428829, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "description": "Перевод организации", "to": "Счет 35383033474447895560"}]
    assert PrintHistory(dict_test, 0).account_code('from') == '1596 83** **** 5199'
    assert PrintHistory(dict_test, 1).account_code('from') == 'NONE **** **** NONE'


def test_print_history_currency():
    dict_test = [{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                  "to": "Счет 64686473678894779589"},
                 {"id": 41428829, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                  "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                  "description": "Перевод организации", "to": "Счет 35383033474447895560"}]
    copy = PrintHistory(dict_test, 0)
    assert (copy.currency() == "31957.58 руб.") is True