#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

#Verifica si se pasa un argumento, si no, solicita el número
if len(sys.argv) < 2:
    number = int(input("Por favor ingresa un número: "))
else:
    number = int(sys.argv[1])

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"El factorial de {number} es {factorial(number)}")
