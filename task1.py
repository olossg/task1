geo_logs = [
['visit1', ['Москва','Россия']],
['visit2', ['Дели', 'Индия']],
['visit3', ['Владимир', 'Россия']],
['visit4', ['Лиссабон', 'Португалия']],
['visit5', ['Париж', 'Франция']],
['visit6', ['Лиссабон', 'Португалия']],
['visit7', ['Тула', 'Россия']],
['visit8', ['Тула', 'Россия']],
['visit9', ['Курск', 'Россия']],
['visit10', ['Архангельск', 'Россия']],
]
for i in range(10):
    if geo_logs[i][1][1] == 'Россия':
        print(geo_logs[i])