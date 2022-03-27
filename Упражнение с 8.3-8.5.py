# Упражнение 8.3
def make_shirt(size):
    print(f"Ваш размер {size}")

make_shirt('L')

# Упражнение 8.4
def make_shirt(txt, size='L'):
    print(f"\nВаш размер {size}?")
    print(f"Да, мой размер {size}, с надписью {txt}.")

make_shirt('I love Python')

# Упражнение 8.5
def describe_city(Russia, England, Ukrain='Украины'):
    print(f"\nМосква столица {Russia}")
    print(f"Лондон столица {England.title()}")
    print(f"Киев столица {Ukrain}")

describe_city('России', 'Англии')



def get_formatted_name(first_name, last_name):
    full_name = f"{first_name}, {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmi', 'netron')
print(musician)

