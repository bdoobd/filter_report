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

    if hlp.check_dir_empty(source_folder):
        print(
            f'Помести исходный .csv файл в папку {source_folder} и снова запусти скрипт')
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
        'test.csv',
        dtype=types_of_columns,
        usecols=list(types_of_columns) + ['Currency amount', 'Acquired',
                                          'Sold', 'Proceeds (EUR)', 'Cost basis (EUR)', 'Gains (EUR)'],
        parse_dates=['Acquired', 'Sold']
    )

    grouped = data.groupby(['Currency name', 'Transaction type'])

    main_table = grouped[['Proceeds (EUR)', 'Cost basis (EUR)', 'Gains (EUR)']].agg(
        'sum')
    add_table = grouped['Gains (EUR)'].agg(
        [('Lost', lambda x: x[x < 0].sum()), ('Gain', lambda x: x[x > 0].sum())])

    print(main_table.join(add_table))

    try:
        hlp.create_folder(ready_folder)
        # TODO: Записать таблицу в файл excel
        main_table.join(add_table).to_excel(ready_folder / ready_file_name)
    except Exception as e:
        print(f'Не удалось создать папку для готового файла.\n')
        print(e)
        sys.exit()
