#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Si el rango no es pasado como argumento, se solicita al usuario
if len(sys.argv) < 2:
    range_input = input("Por favor ingresa el rango (por ejemplo, 5-20): ")
else:
    range_input = sys.argv[1]

#Separar los números desde-hasta
start, end = map(int, range_input.split('-'))

#Calcular y mostrar el factorial para cada número en el rango
for num in range(start, end + 1):
    print(f"El factorial de {num} es {factorial(num)}")