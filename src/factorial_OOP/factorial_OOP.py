#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
class Factorial:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def run(self):
        for i in range(self.min, self.max + 1):
            print(f"{i}! = {self.factorial(i)}")

    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n - 1)

if __name__ == "__main__":
    f = Factorial(4, 8)
    f.run()
