# Курс по Flask и FastAPI от [GeekBrains](https://gb.ru)

Содержание:
- [Настройка виртуального окружения](#настройка-виртуального-окружения)
- [Запуск скриптов](#запуск-скриптов)
- [Ссылки на ДЗ по семинарам с заданиями](#ссылки-на-дз-по-семинарам-с-заданиями)

В данном репозитории собраны выполненные мной ДЗ с семинаров [GeekBrains](https://gb.ru) по базам данных и SQL.

Все выполненные ДЗ лежат в директориях с названиями

`hw_<номер_занятия>`

Все модули отформатированы инструментом [Ruff](https://docs.astral.sh/ruff/) по настройкам в [ruff.toml](./ruff.toml)

## Настройка виртуального окружения

Для настройки виртуального окружения используйте команду 

`py -m venv <название_виртуального_окружения>`

(`python -m venv <название_виртуального_окружения>` на Windows или `python3 -m venv <название_виртуального_окружения>` на Linux, если основная команда не работает)

После этого, активируйте виртуальное окружение командой для вашей ОС.

Для установки необходимых зависимостей, при активном виртуальном окружении выполните команду

`pip install -r requirements.txt`

[Список зависимостей](./requirements.txt):

| Библиотека | Версия |
|---|---|
| Flask | >=3.0.0 |
| ruff | >=0.1.7 |
| Faker | >=20.1.0 |

Виртуальное окружение настроено!

## Запуск скриптов

Для запуска необходимого скрипта можно использовать два способа:

1. Запустить необходимый скрипт из директории, в которой он находится командой `py <файл>` (`python <файл>` на Windows или `python3 <файл>` на Linux, если основная команда не работает).
2. Изменить первую строку файла [wsgi.py](wsgi.py) на необходимый пакет и модуль, из которых будет импортироваться переменная `app`, и выполнить команду `flask run` для Flask, которая запускает сервер Flask.

## Ссылки на ДЗ по семинарам с заданиями:

1. [Семинар 1](./hw_1/README.md)
2. [Семинар 2](./hw_2/README.md)
3. [Семинар 3](./hw_3/README.md) 
