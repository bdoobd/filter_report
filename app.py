import pandas as pd
import numpy as np
from pathlib import Path
import helper as hlp
import sys

source_folder = Path('./source')
ready_folder = Path('./ready')
ready_file_name = hlp.get_file_name()

if __name__ == '__main__':
    try:
        hlp.create_folder(source_folder)
    except Exception as e:
        print(e)
        print('Скрипт закончил работу.')
        sys.exit()

    while hlp.check_dir_empty(source_folder):
        try:
            print('Не найден исходный файл для работы')
            again = input(
                f'Помести исходный .csv файл в папку {source_folder} и нажми ENTER\n')
        except KeyboardInterrupt:
            print('Отмена работы скрипта')
            sys.exit()

    while True:
        try:
            csv_name = input('Укажи имя файла без расширения: ')

            csv_file = source_folder / (csv_name + '.csv')

            if not csv_file.exists():
                print(f'Файл {csv_file} не найден, попробуй ещё раз\n')
                continue
            else:
                break
        except KeyboardInterrupt:
            print('\nВыход. Скрипт закончил работу')
            sys.exit()
        except Exception as e:
            print(e)

    print(f'Файл {csv_file} найден, начинаем обработку файла ....')

    types_of_columns = {
        'Currency name': 'category',
        'Transaction type': 'category',
    }

    data = pd.read_csv(
        csv_file,
        dtype=types_of_columns,
        usecols=list(types_of_columns) + ['Currency amount', 'Acquired',
                                          'Sold', 'Proceeds (EUR)', 'Cost basis (EUR)', 'Gains (EUR)'],
        parse_dates=['Acquired', 'Sold']
    )

    negatives = data.loc[data['Gains (EUR)'] <= 0]
    positives = data.loc[data['Gains (EUR)'] > 0]

    negative_grouped = negatives.groupby(['Currency name', 'Transaction type'])
    positive_grouped = positives.groupby(['Currency name', 'Transaction type'])

    negative_sums = negative_grouped[[
        'Proceeds (EUR)', 'Cost basis (EUR)', 'Gains (EUR)']].agg('sum')
    positive_sums = positive_grouped[[
        'Proceeds (EUR)', 'Cost basis (EUR)', 'Gains (EUR)']].agg('sum')

    negative_sums.loc['TOTAL', :] = negative_sums.sum().values
    positive_sums.loc['TOTAL', :] = positive_sums.sum().values

    try:
        hlp.create_folder(ready_folder)
        with pd.ExcelWriter(ready_folder / ready_file_name) as writer:
            positive_sums.to_excel(writer, sheet_name='Wins')
            negative_sums.to_excel(writer, sheet_name='Losts')
    except Exception as e:
        print(f'Не удалось создать папку для готового файла.\n')
        print(e)
        sys.exit()
    else:
        print(f'Файл {ready_folder / ready_file_name} успешно создан')
