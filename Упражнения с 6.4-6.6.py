# Упражнение 6.4
# Записать задание 6.3 не через вывод а методом цикла
golosaryy = {'Списки': 'Списки нужны для хранинея данных', 'Цикл': 'Циклы: нужны для автоматизации рутиных задач',
             'Кортежи': 'Кортежи как списки только в них данные нельзя менять', 'print': 'print для вывода данных на экран',
             'Input': 'Input считывает данные с клавиатурыёт\n'
             }
for key, value in golosaryy.items():
    print(f"\n'key': {key}")
    print(f"\n'value': {value}")

# Упражнение 6.5 Реки
river = {'nile': 'egypt', 'volga': 'Russia', 'kura': 'Georgia'}

for key, value in river.items(): # Используем цикл для вывода сообщения с упоминанием карждой реки и страны
    print(f"The {key.title()} runs through {value.title()}\n")

for key in river.keys(): # Выводим название всех рек
    print(key.title())

for value in river.values():# Вывод названий стран
    print(value.title())

# Упражнение 6.6
favorite_languages = {
    'jenya': 'python',
    'edward': 'C',
    'nikita': 'java',
    'yura': 'ruby',
    }

print(f"{'jenia'}, примите  участие в опросе")
print(f"{'edward'}, примите участие в опросе")
print(f"{'nikita'}, спасибо что риняли участие в опросе")
print(f"{'yura'}, спасибо за участие и выбор вашего языка {'ruby'}")
