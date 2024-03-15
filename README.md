# Скрипт для группировки csv файла в MS Excel

Скрипт тестировался на Python 3.10.12 Ubuntu Server 22.04.4 LTS

- Склонировать репозиторий или
- Скачать архив и распаковать

## Структура файлов

В корневой папке со скриптом создаётся (если отсутствует) вложенная папка source для файлов .csv. Если папка не была создана при запуске скрипта, она создаётся и скрипт заканчивает работу с уведомлением о том, что в папку source надо положить исходный файл .csv
Так же в корневой папке создаётся (если отсутствует) вложенная папка ready в которую записываются готовые табличные файлы MS Excel

## Запуск скрипта

В терминале перейти в папку со скриртом и запустить _pyhon3 app.py_ **(Linux / MAC OS X)** или _python.exe app.py_ **(Windows)**