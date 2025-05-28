import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(lower, upper):
    return [num for num in range(lower, upper + 1) if is_prime(num)]

def parse_arguments():
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            return 1, 50
        elif len(args) == 1:
            return 1, int(args[0])
        elif len(args) >= 2:
            lower = int(args[0])
            upper = int(args[1])
            if lower > upper:
                raise ValueError
            return lower, upper
    except ValueError:
        print("Error: argumentos inválidos.")
        sys.exit(1)

def leer_rango():
    try:
        lower = int(input("Ingrese el valor inferior del rango: "))
        upper = int(input("Ingrese el valor superior del rango: "))
        if lower > upper:
            print("Error: el valor inferior no puede ser mayor que el superior.")
            sys.exit(1)
        return lower, upper
    except ValueError:
        print("Error: debe ingresar números enteros.")
        sys.exit(1)

def main():
    usar_entrada_manual = input("¿Desea ingresar el rango manualmente? (s/n): ").lower()

    if usar_entrada_manual == 's':
        lower, upper = leer_rango()
    else:
        lower, upper = parse_arguments()

    primes = find_primes(lower, upper)
    print(f'\nNúmeros primos entre {lower} y {upper}:\n')
    print(' '.join(map(str, primes)))

if __name__ == "__main__":
    main()
