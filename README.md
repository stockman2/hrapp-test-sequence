# Набор тестовых заданий

## 1. Git
0. Скопируйте себе удаленный репозиторий `https://github.com/GorillazZz1/hrapp-test-sequence`.
1. Создайте новую ветку `feature/<your-name>`, наследуюясь от ветки `develop`.
2. В файле `TEST.txt` напишите ваше имя и возраст.
3. Отправьте вашу ветку и обновленный файл `TEST.txt` на удаленный репозиторий.
4. Попробуйте создать Pull Request.

должно получится что-то вроде такого **TODO: скриншот с результатом**
###### Ref:
- https://training.github.com/downloads/ru/github-git-cheat-sheet/


## 2. Python
Напишите функцию, на вход которой приходит **строка в формате json** заданного вида.
А функция возвращает json содержащий в поле `data` только события, которые произошли не более чем 10 днями ранее или позднее от **01.09.2021**.
##### Input
```json
{
    "user_id": 123,
    "data": [
        {
            "text": "Событие №1",
            "date": "2021-05-30"
        },
        {
            "text": "Событие №2",
            "date": "2021-08-31"
        },
        {
            "text": "Событие №3",
            "date": "2021-09-12"
        }
    ]
}
```
##### Output
```json
{
    "user_id": 123,
    "data": [
        {
            "text": "Событие №2",
            "date": "2021-08-31"
        }
    ]
}
```
###### Ref:
- https://docs.python.org/3/library/json.html
- https://docs.python.org/3/library/datetime.html


## 3. Jinja
Напишите jinja2 шаблон выводящий по заданному массиву `{{ main_data.data }}` только имена людей для которых поле `sum` больше 100, с указанием суммы
##### Input
```json
{
    "data": [
        {
            "name": "Саша",
            "sum": "42,50"
        },
        {
            "name": "Оля",
            "sum": "100,50"
        },
        {
            "name": "Сережа",
            "sum": "10 000,00"
        }
        ...
    ]
}
```
##### Output
```string
Оля - 100,50
Серёжа - 10 000,00
```
###### Ref:
- https://jinja.palletsprojects.com/en/3.0.x/templates/


## 4*. Easy-Afina

https://developers.sber.ru/docs/ru/salute/python-framework/framework_scenario

