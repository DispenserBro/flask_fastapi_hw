# Домашнее задание по 5 семинару

[Общие сведения](../)

## Задания

- [Задание](#задание-с-семинара), [скрипт](./task.py), [модели](./pydantic_models.py)

### Задание с семинара

- `Напишите RESTful API по желанию с методами GET, POST, PUT, DELETE`

- `Для отображения данных по GET-запросам использовать шаблоны Jinja2`

#### Описание решения

Для создания API я решил выбрать API с информацией о песнях.

В модели Pydantic создание экземпляра песни можно описать так:

`Song(id=<id: int>, name=<name: str>, author=<author: str>, genre=<genre: str>[, description=<description: str>])`

Для хранения файлов используется файл [data.json](./data.json).
Его можно представить, как JSON-ответ от API доступа к БД.
При запуске сервера, из него берутся сохранённые данные о песнях.
При добавлении, изменении или удалении песни, все эти действия фиксируются в данном файле.

Для сохранения изменений в файл, используется библиотека [aiofiles](https://pypi.org/project/aiofiles/).
В функции [commit_changes](./task.py#L29) содержимое списка `music` преобразуется в JSON-формат и сохраняется в файл.

API позволяет отправлять запросы по следующим адресам:

- `<host>/`, методы:
    - `GET`: показывает список всех песен с возможностью перейти на страницу каждой песни

- `<host>/music`, методы:
    - `POST`: позволяет добавить песню в соответствии с моделью

- `<host>/music/<song_id>`, методы:
    - `GET`: показывает страницу песни по её `id`
    - `PUT`: позволяет изменить данные песни, кроме её `id`
    - `DELETE`: позволяет удалить песню по её `id`