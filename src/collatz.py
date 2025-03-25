import matplotlib.pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        steps += 1
    return steps

x = list(range(1, 10001))
y = [collatz_steps(n) for n in x]

plt.scatter(x, y, s=1)
plt.xlabel("Número Inicial")
plt.ylabel("Número de Iteraciones")
plt.title("Conjetura de Collatz para 1-10000")
plt.show()
