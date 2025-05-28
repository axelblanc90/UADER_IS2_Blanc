# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: old_primes.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 18:42:35 UTC (1746556955)


import sys

import os
os.system("cls")

try:
    if len(sys.argv) == 2:
        lower = 1
        upper = int(sys.argv[1])

    elif len(sys.argv) >= 3:
        lower = int(sys.argv[1])
        upper = int(sys.argv[2])

    else:
        lower = 1
        upper = 50

    if lower>upper:
        print("ingrese los valores en order para poder calcular")
        exit()
except:
    print("argumento invalido")
    exit()

print('Numeros primeos entre %d y %d son: \n' % (lower, upper))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print('%d ' % num)
