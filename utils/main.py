from utlis.class_print_history import PrintHistory
from utlis.functions import sorted_date

sort_list = sorted_date()

for i in range(5):
    copy = PrintHistory(sort_list, i)
    print((
        f'\n{copy.date_print()} {copy.print_line('description')}\n{(copy.account_code('from'))} ->'
        f'{copy.account_code('to')}\n{copy.currency()}\n'))

