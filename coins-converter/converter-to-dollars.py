def conversor(tipo_pesos, valor_dolar):
    dinero = input("¿Cuánto dinero " + tipo_pesos + " tienes?: ")
    dinero = float(dinero)
    dolares = dinero / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = """
Bienvenido al conversor de monedas 🙂

1. Soles
2. Pesos Argentinos
3. Pesos Mexicanos

Elige una opción: """

opcion = input(menu)


if opcion == '1':
    conversor("Soles", 3.95)

elif opcion == '2':
    conversor('Pesos Argentinos', 65)

elif opcion == '3':
    conversor('Pesos Mexicanos', 3875)
else:
    print('Ingresa una opción correcta')
