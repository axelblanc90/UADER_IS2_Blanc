import sys

MAX_LIMIT = 600525  # Límite superior permitido para el rango de búsqueda de primos


def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # optimización: solo hasta raíz cuadrada de n
        if n % i == 0:
            return False
    return True


def imprimir_primos(lower, upper):
    """Imprime todos los números primos en el rango [lower, upper]."""
    print(f"Números primos entre {lower} y {upper}:")
    for num in range(lower, upper + 1):
        if es_primo(num):
            print(num, end=' ')
    print()  # Salto de línea al final


def leer_rango():
    """Solicita al usuario los valores del rango y valida las restricciones."""
    try:
        lower = int(input("Ingrese el valor inferior del rango: "))
        upper = int(input("Ingrese el valor superior del rango: "))

        if lower < 0:
            print("Error: el valor inferior no puede ser negativo.")
            sys.exit(1)

        if upper > MAX_LIMIT:
            print(f"Error: el valor superior no puede ser mayor a {MAX_LIMIT}.")
            sys.exit(1)

        if lower > upper:
            print("Error: el valor inferior no puede ser mayor que el superior.")
            sys.exit(1)

        return lower, upper
    except ValueError:
        print("Error: debe ingresar números enteros.")
        sys.exit(1)


def parse_arguments():
    """Procesa argumentos de línea de comandos y valida las restricciones."""
    try:
        args = sys.argv[1:]

        if len(args) == 0:
            return 1, 50  # Valores por defecto
        elif len(args) == 1:
            upper = int(args[0])
            if upper < 0:
                raise ValueError("El valor superior no puede ser negativo.")
            if upper > MAX_LIMIT:
                raise ValueError(f"El valor superior no puede ser mayor a {MAX_LIMIT}.")
            return 1, upper
        elif len(args) >= 2:
            lower = int(args[0])
            upper = int(args[1])

            if lower < 0:
                raise ValueError("El valor inferior no puede ser negativo.")
            if upper > MAX_LIMIT:
                raise ValueError(f"El valor superior no puede ser mayor a {MAX_LIMIT}.")
            if lower > upper:
                raise ValueError("El valor inferior no puede ser mayor que el superior.")
            return lower, upper
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """Función principal que ejecuta el programa."""
    usar_manual = input("¿Desea ingresar el rango manualmente? (s/n): ").strip().lower()

    if usar_manual == 's':
        lower, upper = leer_rango()
    else:
        lower, upper = parse_arguments()

    imprimir_primos(lower, upper)
    


if __name__ == "__main__":
    main()
