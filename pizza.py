# пишем функцию, которую будем запускать в файле ( Упражнения с 8.15 - 8.17 для примера
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
