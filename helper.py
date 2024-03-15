from datetime import datetime
import sys


def get_file_name() -> str:
    date_format = datetime.now().strftime('%Y-%m-%d-%H-%M')
    return f'Generated_report_{date_format}.xlsx'


def create_folder(folder_path: str) -> None:
    if not folder_path.exists():
        try:
            folder_path.mkdir()
        except Exception:
            raise Exception('Не удалось создать папку для исходных файлов.')


def check_dir_empty(directory: str) -> bool:
    return not any(directory.iterdir())


def ask_file_name(src: str) -> str:
    while True:
        try:
            csv_name = input('Укажи имя файла без расширения: ')

            csv_file = src / (csv_name + '.csv')

            if not csv_file.exists():
                print(f'Файл {csv_file} не найден, попробуй ещё раз\n')
                continue
            else:
                return csv_file
        except KeyboardInterrupt:
            print('\nВыход. Скрипт закончил работу')
            sys.exit()
        except Exception as e:
            print(e)
