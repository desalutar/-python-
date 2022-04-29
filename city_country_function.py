# Упражнение 11.1
from city_function import get_city_country

print("Нажмите 'q' чтоб выйти")
while True:
    country = input("Введите название страны.")
    if country == 'q':
        break
    city = input("Введите название столицы.")
    if city == 'q':
        break

    city_function = get_city_country(country, city)
    print(f"\tВаш ввод: {city_function}.")
