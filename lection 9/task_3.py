# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


with open("test_file/task_3.txt", 'r') as price_doc:
    prices_list = price_doc.readlines()
    prices_each = 0
    prices_sum = []
    for idx, line in enumerate(prices_list):
        line = line.replace('\n', '')
        if line == '':
            prices_sum.append(prices_each)
            prices_each = 0
            continue
        prices_each += int(line)
    three_most_expensive_purchases = sum(sorted(prices_sum)[-3:])

assert three_most_expensive_purchases == 202346
