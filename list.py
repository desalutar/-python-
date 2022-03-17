#добавление елементов в конец и произвольную позицию списка
mytopcar = ['Bmw', 'Mersedes', 'Volvo']
print(mytopcar)
mytopcar.append('Ferrari')
print(mytopcar)
mytopcar.insert(2, 'Lada')
print(mytopcar)

last_owned = mytopcar.pop()
print(f"Моя последняя покупка это {last_owned.title()}.")

furst_owned = mytopcar.pop(2)
print(f"Моя последняя покупка это {furst_owned.title()}.")


