# def make_pizza(*toppings):  # Звездочка создает кортеж с именем toppings
#     """Вывод списка заказанных топпингов."""
#     print("\nMake a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(size, *toppings):
#     """Выводит описание пиццы"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)


# Упражнение 8.12
# def delicious_sandwich(*toppings):
#     print("\nВаш сэндвич c: ")
#     for topping in toppings:
#         print(f"- {topping}")
#
# delicious_sandwich('Курицей и грибами')
#
# def dellicions_sandwich(*toppings):
#     print("\nТакже у нас есть сэндвичи с: ")
#     for topping in toppings:
#         print(f"- {topping}")
#
# dellicions_sandwich('Ветчина сыр', 'Чешские колбаски', 'Веган')
#
# def delli_sandwich(*toppings):
#     print("\nВы поменяли свой выбор и выбрали с:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# delli_sandwich('Веган сендвич')

# Упражнение 8.13
# def user_prof(first, last, **kwargs):  # Две звездочки это создание пустого словаря
#     kwargs['first name'] = first  # тут мы пихаем все параметры сверху в словарь
#     kwargs['last name'] = last
#     return kwargs  # возвращаем значение словаря
#
# prof_users = user_prof('Steve', 'Jobs',  # сперва определили что first и last входят в словарь то они и стали ключом
#                        location='San Francisco',  # непосредственно записываем что будет в словаре ключ значение
#                        field='genius')
# print(prof_users)

# Упражнение 8.14
# def make_car(name, model, color, equipment, **kwargs):
#     kwargs['name'] = name
#     kwargs['model'] = model
#     kwargs['equipment'] = equipment
#     kwargs['color'] = color
#     return kwargs
#
# car = make_car('Subaru', 'outback',  # Пример словаря я взял из книги
#                equipment='Full', color='blue',
#                tow_package='available')
# print(car)