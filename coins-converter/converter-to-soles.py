dollars = input('¿Cuántos dólares tienes?: ')
dollars = float(dollars)
valor_sol = 0.26
soles = dollars / valor_sol
soles = round(soles, 2)
soles = str(soles)

print('Tienes PEN ' + soles + ' soles')
