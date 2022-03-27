# def get_formatted_name(first_name, last_name, middle_name='',):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimmi', 'milk')
# print(musician)



# def build_person(first_name, last_name):  # Указываем параметром значение словаря в функции
#     person = {'first': first_name, 'last': last_name}  # словарь значение которого является параметр функции
#     return person
#
# musician = build_person('jimmi', 'hendrix')  # указываем аргумент нашему значению
# print(musician)
#
#
# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('alla', 'ivanova', age=27)
# print(musician)



# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# Упражнение 8.6
# def city_country(city_name=None, country_name=None):  # создаем функцию для получения названия города и страны
#     all_name = f"{country_name} {city_name}"
#     ci_name = input("Введите название города: ")
#     co_name = input("Введите название страны: ")
#     print(f"Ваша страна {co_name}, а город {ci_name}")  # а так же его вывода
#     return all_name.title()
#
# city_country()

# Упражнение 8.7
# def make_album(singer_name, name_album, number_tracks_album=None):
#     person = {'singer': singer_name, 'album': name_album, 'tracks in album': number_tracks_album}
#     if number_tracks_album:
#         person['tracks in album'] = number_tracks_album
#     return person
#
# musician = make_album('Maks Korj', '2012', '17')
# print(musician)



# Упражнение 8.8
# def make_album(singer_name, name_album, number_tracks_album=None):
#     person = {'Исполнитель': singer_name, 'Альбо': name_album, 'кол-во песен': number_tracks_album}
#     if number_tracks_album:
#         person['tracks in album'] = number_tracks_album
#     return person
#
# while True:
#     #print("Нажмите 'q' для выхода: ")
#
#     s_name = input("Введите имя исполнителя или нажмите 'q' для выхода:")
#     if s_name == 'q':
#         break
#     na_name = input("Введите название альбома")
#     if na_name == 'q':
#         break
#     nta = input('Сколько песен в альбоме? ')
#     if nta == 'q':
#         break
#
#     album_make = make_album(s_name, na_name, nta)  # запускаем функцию, передаём в нее то что введет пользователь
#     print(f"\n{album_make}")