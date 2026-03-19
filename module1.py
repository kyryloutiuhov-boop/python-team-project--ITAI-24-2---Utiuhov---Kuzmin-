import math
import numpy as np
import matplotlib.pyplot as plt

x = float(input("Введіть значення x: "))

if x == 0:
    print("Помилка: ділення на нуль!")
else:
    y = x + 1/x - 2 * math.sin(math.pi * x / 2)
    y = abs(y)
    print("Значення функції y =", y)

x_1 = np.linspace(-10, 10, 100)
x_1 = x_1[x_1 != 0]

y_1 = abs(x_1 + 1/x_1 - 2 * np.sin(np.pi * x_1 / 2))

plt.plot(x_1, y_1)
plt.grid()
plt.title("y = |x + 1/x - 2sin(pi*x/2)|")
plt.xlabel("x")
plt.ylabel("y")
plt.show()