import random


longitud = random.randint(1, 8)
binario = ''.join(str(random.randint(0, 1)) for _ in range(longitud))

decimal = 0
for digito in binario:
    decimal = decimal * 2 + int(digito)

print('Numero binario generado:', binario)
print('Conversion a decimal:', decimal)
