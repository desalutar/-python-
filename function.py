# этот модуль я создал для задания 8.15-8.17.py
# копируем сюда все с Упражнения 8.9-8.11
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ('hannah', 'ty', 'margot')  # создается список
greet_users(usernames)  # список передается в функцию где она запускает цикл



unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    concurrent_design = unprinted_designs.pop()
    print(f"Printing model: {concurrent_design}")
    completed_models.append(concurrent_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




#Упражнение 8.9
def show_message(message):  # создаем функцию, которая будет вызывать список коротких сообщений
    for messages in message:
        print(messages)

message = ['Как дела?', 'Что нового?', 'Какая погода у вас?', 'Чем занимаетесь?']  # список коротких сообщений
show_message(message)


# Упражнение 8.10
# Перенесение из одного списка в другой внутри функции

def show_short_message(show_message, send_messages):
    while show_message:
        message = show_message.pop()
        print(f"Не перенесенные сообщение: {message}")
        send_messages.append(message)

def send_message_oww(send_messages):
    print("\nПеренесенные сообщения")
    for send_message in send_messages:
        print(send_message)

show_message = ['Как дела?', 'Что нового?', 'Какая погода у вас?', 'Чем занимаетесь?']  # список с сообщениями
send_message = []  # пустой список

show_short_message(show_message, send_message)
send_message_oww(send_message)


# Упражнение 8.11
show_short_message(send_message[:], show_message)
print(show_message)
print(send_message)