# import pizza # Импортируем модуль с другого файла

# pizza.make_pizza(16, 'pepperoni')  # При вызове пишем имя модуля и имя функции
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# Еще одна версия импортирования функции из другого модуля
# from pizza import make_pizza  # Импортируем только функцию не весь модуль, а только функцию из него

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# from pizza import make_pizza as mp  # Даем псевдоним функции make_pizza называя ее mp с помощью as

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')



# import pizza as p # Импортируем модуль но теперь уже называя ее p

# p.make_pizza(16, 'pepperoni')  # вызываем по псевдониму модуля точка имя функции
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# from pizza import *  # тут * импортирует все что есть в модуле
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Упражнение 8.15
# from function import greet_users as gu
# usernames = ('hannah', 'ty', 'margot')
# gu(usernames)



# # Упражнение 8.16.1
# import function  # Использование только import
# # когда импортируешь функцию связанную не забудь и словарь
# # если он на него ссылается
# show_message = ['Как дела?', 'Что нового?', 'Какая погода у вас?', 'Чем занимаетесь?']
# send_message = []
# function.show_short_message(show_message, send_message)
# function.send_message_oww(send_message)

# # Упражнение 8.16.2
#from function import show_completed_models, completed_models
# импортируем с модуля только две функции
#show_completed_models(completed_models)

# # Упражнение 8.16.3
# Импортируем модуль используя , псевдоним для функции
# from function import greet_users as gu
# usernames = ('hannah', 'ty', 'margot')
# gu(usernames)

# # Упражнение 8.16.4
# import function as fun
# # Импортируем с модуля с помощью псевдонима самого модуля
# show_message = ['Как дела?', 'Что нового?', 'Какая погода у вас?', 'Чем занимаетесь?']
# send_message = []
# fun.show_short_message(show_message, send_message)
# fun.send_message_oww(send_message)

# Упражнение 8.16.5
# Импортируем из модуля все благодаря *
# from function import *
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Конец 8 главы