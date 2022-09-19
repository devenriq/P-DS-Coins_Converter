import random


def run():
    num_aleatorio = random.randint(1, 100)
    num_elegido = int(input('Elige un número al azar: '))
    while num_elegido != num_aleatorio:
        if num_elegido < num_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')

        num_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()
