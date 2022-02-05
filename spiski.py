#добавление елементов в конец и произвольную позицию списка
#удаление елемнетов из списка
mytopcar = ['Bmw', 'Mersedes', 'Volvo']
print(mytopcar)
mytopcar.append('Ferrari')
print(mytopcar)
mytopcar.insert(2, 'Lada')
print(mytopcar)

mytopcar = ['Bmw', 'Mersedes', 'Volvo']
print(mytopcar)

soopl = ('Bmw')
mytopcar.remove(soopl)
print(mytopcar)
print(f"\n Данная марка {soopl.title()} не подошла в мою коллекцию")