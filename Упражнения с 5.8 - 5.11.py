# Все упражнения с книги Эрик Мэтиз изучаем PYTHON
# 5.8 Hello Admin
helloadmin = ['admin', 'gor', 'stussy']
if 'admin' in helloadmin:
    print('Hello admin, would you like to see a status report?')
if 'gor' in helloadmin:
    print('Hello Gor, thank ypu for loggin in again')
if 'stussy' in helloadmin:
    print('Hello Stussy, thank ypu for loggin in again\n')

# 5.9 Без пользователей
huiloadmin = []
if 'alex' in huiloadmin:
    print('asdfghjk')
else:
    print("We need to ind some users\n")

# 5.10 Проверка имен пользователей
current_users = ['qwerty', 'alisa', 'oleg', 'egor', 'bob', 'dmitro']
new_users = ['alex', 'Alisa', 'jenya', 'egor', 'bob', 'nasteisha']
for current_user in current_users:
    if current_user in new_users:
        print(f"Имя {current_user} занято, выберите другое")
    elif new_users in current_users:
        print('Имя занято')
print('Выберите из доступных')
print([i for i in new_users if i not in current_users])# Вывод свободных имен
# 5.11 Порядковые числительные

