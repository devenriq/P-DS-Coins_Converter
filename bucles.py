def run():
    LIMIT = 1000000

    counter = 0
    potencia_2 = 2 ** counter
    while potencia_2 < LIMIT:
        print('2 elevado a ' + str(counter) + ' es igual a ' + str(potencia_2))
        counter = counter + 1
        potencia_2 = 2**counter


if __name__ == '__main__':
    run()
