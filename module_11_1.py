# Тема "Обзор сторонних библиотек Python"
from requests import get, ConnectionError
import numpy as np
import pandas as pd
from random import randint


#  1.Библиотека requests. Вывод моего местожительства на карте Яндекс

URL = "https://static-maps.yandex.ru/1.x/"
params = {"ll": "30.232173,59.949579",
          "spn": "0.016457,0.00619",
          "l": "map"}
try:
    response = get(URL, params=params)
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)

# 2.Библиотека numpy. Вычисления суммы элементов массива, поиск минимального и максимального элемента

matrix = np.random.randint(-100, 100, size=(4, 4))

print(matrix)
print()
print(f'{matrix.sum()} - сумма всех элементов массива')
print(f'{matrix.min()} - минимальный элемент массива')
print(f'{matrix.max()} - максимальный элемент массива')
# Запись в Exel
df = pd.DataFrame(matrix)
df.to_excel(excel_writer="./test.xlsx", index=False)
print()

# 3.Библиотека pandas. График инфляции за полгода

print()
io = 'https://cbr.ru/Queries/UniDbQuery/DownloadExcel/132934?FromDate=04%2F28%2F2024&ToDate=10%2F25%2F2024&posted=False'
df = pd.read_excel(io)
print(df)
