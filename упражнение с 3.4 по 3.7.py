#упражнение 3.4
list = ['Stas', 'Egor', 'Max']
print(list)

print("Я решил открыть ресторан и приглашаю всех.")

message = f"Приглашаю тебя {list[0].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[1].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[2].title()} на ужин в 20:00"
print(message)

print(list[2])
list[2] = 'Oleg'

message = f"Приглашаю тебя {list[2].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[0].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[1].title()} на ужин в 20:00"
print(message)

print("Заказал стол побольше в ресторане и придут больше гостей ")
list.insert(0, 'Nikita')
list.insert(2, 'Alex')
list.append('Dmitro')

message = f"Приглашаю тебя {list[0].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[1].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[2].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[3].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[4].title()} на ужин в 20:00"
print(message)

message = f"Приглашаю тебя {list[5].title()} на ужин в 20:00"
print(message)

print("Нихуя не получилось заказать идут только двое)")
popend_list = list.pop(0)
print(f"К сожалению ты не идешь в ресторан {popend_list.title()}")

tyu_list = list.pop(1)
print(f"К сожалению ты не идешь в ресторан {tyu_list.title()}")

asd_list = list.pop(2)
print(f"К сожалению ты не идешь в ресторан {asd_list.title()}")

zxc_list = list.pop()
print(f"К сожалению ты не идешь в ресторан {zxc_list.title()}")

message = f"С тобой {list[0].title()} и Егором мы идем"
print(message)
message = f"С тобой {list[1].title()} и Стасом мы идем"
print(message)

#del list[0]
#print(list)
#del list[0]


print(list)


len(list)










