#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

#en esta parte delimita un maximo y minimo de numeros
lower = 1
upper = 500


print("Prime numbers between", lower, "and", upper, "are:")


 for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
        #si el numero es dibvisible por cualquier numero de i,no es un num primo
           if (num % i) == 0:
               break
       else:
           print(num)
