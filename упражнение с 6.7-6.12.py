# Упражнение 6.7
# Создаем 3 словаря с данными о 3 людях
people_0 = {'first_name': 'Alex', 'last_name': 'Ivanov', 'Age': '25', 'City': 'Moscow'}
people_1 = {'first_name': 'Vano', 'last_name': 'Cicilidze', 'Age': '30', 'City': 'Tbilisi'}
people_2 = {'first_name': 'Katya', 'last_name': 'Kurova', 'Age': '19', 'City': 'Voronej'}
# Сохр все словари в один список
peoples = [people_0, people_1, people_2]
for people in peoples:  # Выводим ключи и значения из списка
    print(people)

# Упражнение 6.8
# проделываем тоже самое только теперь с животными
pet_0 = {'type_of_animal': 'dog', 'name_animals': 'bobik', 'Age': '5', 'owner_name': 'Alex'}
pet_1 = {'type_of_animal': 'cat', 'name_animals': 'markiz', 'Age': '2', 'owner_name': 'Vano'}
pet_2 = {'type_of_animal': 'rabbit', 'name_animals': 'mikky', 'Age': '3', 'owner_name': 'Katya'}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(pet, '\n')

# Упражнение 6.9
favorite_places = {
    'Moscow': 'the Red Square and Gorky Park',
    'Tbilisi': 'freedom square' 'Mtskheta',
    'New-York': 'central park' 'Wall Street',
}
print(f"Alex was in {'Moscow'}, his favorite place is{favorite_places['Moscow']}")
print(f"Vano was in {'Tbilisi'}, his favorite place is{favorite_places['Tbilisi']}")
print(f"Katya was in {'Ney-York'}, his favorite place is{favorite_places['New-York']}\n")

# Упражнение 6.10
# Изменить урп. 6.2 , так чтоб у каждого человека было несколько любимых чисел
love_numer = {
    'Viktor': ['55', '13', '77', '90'],
    'Shtefan': ['34', '0', '11', '74'],
    'Lilit': ['999', '123', '67', '88'],
}
for name, languages in love_numer.items():
    print(f"\nAt {name.title()}'s favorite numbers are:")  # Пишем вывод ключей
    for language in languages:
        print(f"\t{language.title()}")  # Пишем вывод значений

# Упражнение 6.11
cities = {
    'Kiev': {
        'Country': 'Ukrain',
        'Population': '2 954 564 people, ',
        'Fact': "One of the symbols of Kiev is a chestnut leaf",
    },

    'Moscow': {
        'Country': 'Russia',
        'Population': '12 655 050 people, ',
        'Fact': "From 1712 to 1918 Moscow was deprived of the status of the capital",
    },

    'Tokyo': {
        'Country': 'Japan',
        'Population': '14 049 146 people, ',
        'Fact': "The Emperor's house is located in Tokyo"
    },
}
# я хотел чтоб вывод был таким же как и в коде все записано однако не нашел как это сделать
if 'Kiev' in cities:
    print(f"Name of the city: {'Kiev'}")# {cities['Kiev']}")
    print(f"{cities['Kiev']}\n")
if 'Moscow' in cities:
    print(f"Name of the city: {'Moscow'}")#{cities['Moscow']}")
    print(f"{cities['Moscow']}\n")
if 'Tokyo' in cities:
    print(f"Name of the city: {'Tokyo'}")# {cities['Tokyo']}")
    print(f"{cities['Tokyo']}")
# print(f"Name of the city{cities,}\n{cities['Kiev']}")
