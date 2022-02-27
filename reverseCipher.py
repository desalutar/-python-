# Программа взята из книги Cracking Codes with Python
# Ссылка на книгу https://www.nostarch.com/crackingcodes/
# Программа обратного шифрования.

message = '.2202.20.72 угом как нотиП учу я а , ортем моксвоксоМ в театобар ен иматрак аталпо , есабнод ан анйов теди ,охолп есВ'
translated = ''

i = len(message) -1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
