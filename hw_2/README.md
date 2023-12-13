# Домашнее задание по 1 семинару

[Общие сведения](../)

## Задания

- [Задание № 6](#задание-6-с-семинара): [скрипт](./task_6.py)

- [Задание № 7](#задание-7-с-семинара): [скрипт](./task_7.py)

- [Задание № 8](#задание-8-с-семинара): [скрипт](./task_8.py)

- [Задание № 9](#задание-9-с-семинара): [скрипт](./task_9.py)

### Задание 6 с семинара

- `Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"`

- `При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.`

#### Описание решения

В шаблонах для отображения используетс тулкит [Bootstrap](https://getbootstrap.com).
Основной шаблон наследуется от шаблона-обёртки.
В функции-отображении index_post() с формы собираются и анализирутся введённые данные. Если возраст является целым числом и больше `0`, тогда результат считается успешным, фон у уведомления будет зелёным, иначе красным.

### Задание 7 с семинара

- `Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"`

- `При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.`

#### Описание решения

Схема построения шаблонов аналогична предыдущему заданию.
Работа функций аналогична.
Поле ввода дополнительно настроено, чтобы работать с шагом `0.01`
Вычисления разделены для целых и дробных чисел, для дробных числе результат округляется до 5 знаков после запятой.

### Задание 8 с семинара

- `Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"`

- `При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".`

#### Описание решения

Структура абсолютно аналогична примеру из методички по лекции.
Секрет генерируется каждый раз при запуске модуля.
Внутри формы в шаблоне есть отдельный блок для flash-сообщений.

### Задание 9 с семинара

- `Создать страницу, на которой будет форма для ввода имени
и электронной почты`

- `При отправке которой будет создан cookie файл с данными
пользователя`

- `Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.`

- `На странице приветствия должна быть кнопка "Выйти"`

- `При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.`

#### Описание решения

В этом задании используется два шаблона: [login](./templates/forms/login.html) и [greet](./templates/greet.html). 
При использовании правильной почты и пароля, 
происходит перенаправление на страницу с приветствием и создание cookie с именем пользователя. 
При этом, если перейти на страницу приветствия, не войдя на сайт, 
вместо имени пользователя будет выводится `Гость`. 
Также, если пользователь вошёл, будет отображаться кнопка `Выйти`, а если нет, то кнопка `Войти`.

Для произведения этих действий, в скрипте используются три функции-представления:

- Первая выводит главную страницу, проверяет данные пользователя при входе, и создаёт cookie.
- Вторая удаляет cookie при выходе и перенаправляет на главную страницу.
- Третья показывает страницу приветствия, независимо от того, вошёл пользователь или нет.