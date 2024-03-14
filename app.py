import pandas as pd
import numpy as np
from pathlib import Path
import sys

if __name__ == '__main__':
    # TODO: Прочитать файл .csv. Для этого придумать момент с расположением файла или запросом файла у пользователя
    source_folder = Path('./source')

    if not source_folder.exists():
        try:
            source_folder.mkdir()
        except Exception as e:
            print('Не могу создать папку для исходников')
            print(e)
            sys.exit()
        else:
            print(
                f'Помести исходный .csv файл в папку {source_folder} и снова запусти скрипт')
            sys.exit()

    while True:
        csv_name = input('Укажи имя файла без расширения: ')

        csv_file = source_folder / (csv_name + '.csv')

        if not csv_file.exists():
            print(f'Файл {csv_file} не найден, попробуй ещё раз\n')
            continue
        else:
            break

    print(f'Файл {csv_file} найден, начинаем обработку файла ....')
    # data = pd.read_csv('test.csv')
    # data = data.iloc[:, [0, 1, 2, 3, 4, 5, 6, 8]]

    # data['Acquired'] = pd.to_datetime(data['Acquired'])
    # data['Sold'] = pd.to_datetime(data['Sold'])

    # group_by_symbol = data.groupby(['Currency name', 'Transaction type'])

    # group_by_symbol['Gains (EUR)']
