# Все упражнения взяты с кники, Эрик Метиз изучаем Python
# 5.3 Если цвет зеленый то и игрок заработал 5 очков
allien_color = 'green'
if allien_color == 'green':
    print("Вы заработали 5 очков\n")

# 5.3 часть кода где ничего не будет выводиться
colorb = 'green'
if colorb == 'blue':
    print("")

# 5.4 написать цепочку if-else
allien_color = 'blue'
if allien_color == 'green':
    print("Вы заработали 5 очков")
else:
    print('Вы только что заработали 10 очков\n')

# 5.5 Теперь пишем с добавлением elif
allien_color = 'green', 'yellow'
if allien_color == 'green':
    print("Вы заработали 5 очков")
elif allien_color == 'yellow':
    print("Вы заработали 10 очков")
else:
    print("Вы заработали 15 очков\n")

# 5.6 Периоды жизни человека
age = 75
if age < 2:
    print("Вы младенец")
elif age >= 2:
    if age < 4:
        print("Малыш")
    elif age > 4:
        if age < 13:
            print("Ребенок")
        elif age >= 13:
            if age < 20:
                print("Подросток")
            elif age >= 20:
                if age <= 65:
                    print("Взрослый")
                else:
                    print("Вы пожилой человек\n")

# 5.7 Любимый фрукт
favorite_fruits = ['Яблоки', 'Бананы', 'Персики']
if 'Яблоки' in favorite_fruits:
    print("Ты действительно любишь Яблоки!")
if 'Бананы' in favorite_fruits:
    print("Ты действительно любишь Бананы!")
if 'Персики' in favorite_fruits:
    print("Ты действительно любишь Персики!")
