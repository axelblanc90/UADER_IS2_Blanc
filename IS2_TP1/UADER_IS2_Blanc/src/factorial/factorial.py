#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

#Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

#Obtener la entrada desde los argumentos o pedirla al usuario
if len(sys.argv) < 2:
    range_input = input("Por favor, ingrese un número o rango (ejemplo 4-8): ")
else:
    range_input = sys.argv[1]

#Caso 1: Si el argumento tiene un '/', se trata de un rango
if '/' in range_input:
    try:
        start, end = map(int, range_input.split('/'))
    except ValueError:
        print("Error: El rango no está bien formado. Asegúrese de ingresar dos números separados por un '/'.")
        sys.exit(1)  # Salir con un error si el rango no es válido
else:
    # Caso 2: Si es un solo número
    try:
        number = int(range_input)
        # Si el número es negativo, calcular factorial desde 1 hasta el valor absoluto de ese número
        if number < 0:
            start, end = 1, abs(number)  # Cambiar el rango para que empiece en 1
        # Si el número es positivo, calcular factorial desde ese número hasta 60
        else:
            start, end = number, 60
    except ValueError:
        print("Error: La entrada no es un número válido.")
        sys.exit(1)  # Salir con un error si la entrada no es válida

#Calcular los factoriales entre el rango (start, end)
for num in range(start, end + 1):
    print(f"El factorial de {num} es {factorial(num)}")