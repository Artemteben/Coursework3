from utlis.functions import import_json, find_operations_json, executed, filter_executed, sorted_date


def test_import_json():
    assert isinstance(import_json(), list) is True


def test_find_operations_json():
    assert isinstance(find_operations_json(), str) is True
    assert isinstance(find_operations_json(name_json='op.json'), str) is False
    assert isinstance(find_operations_json(name_json='op'), str) is False


def test_executed():
    assert executed({"state": "EXECUTED"}) is True
    assert not executed({"state": "PENDING"}) is True


def test_filter_executed():
    assert ((list(filter_executed())[0])['state'] == "EXECUTED") is True
    assert ((list(filter_executed())[0])['state'] == "Test") is False


def test_sorted_date():
    assert isinstance(sorted_date(), list)
    assert ('2019-12-08' in (sorted_date()[0])['date']) is True