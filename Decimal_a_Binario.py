
numero = input('Ingresa un numero decimal: ')

if not numero.isdigit():
    print('Por favor ingresa un numero decimal valido.')
else:
    decimal = int(numero)

    if decimal == 0:
        binario = '0'
    else:
        binario = ''
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal = decimal // 2

    print('Numero decimal ingresado:', numero)
    print('Conversion a binario:', binario)
