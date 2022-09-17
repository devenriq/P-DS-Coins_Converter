menu = """
Bienvenido al conversor de monedas 🙂

1. Soles
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    soles = input('¿Cuántos soles tienes?: ')
    soles = float(soles)
    valor_dolar = 3.95
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('Tienes $'+dolares + ' dólares')

elif opcion == '2':
    soles = input('¿Cuántos pesos argentinos tienes?: ')
    soles = float(soles)
    valor_dolar = 65
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)

    print('Tienes $'+dolares + ' dólares')

elif opcion == '3':
    soles = input('¿Cuántos pesos mexicanos tienes?: ')
    soles = float(soles)
    valor_dolar = 3875
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $'+dolares + ' dólares')

else:
    print('Ingresa una opción correcta')
