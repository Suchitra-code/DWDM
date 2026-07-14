import numpy as np
a = np.arange(12).reshape(4, 3) ** 2
print("Let's consider an array:\n", a)
print()
for i in a:
    print(i * 2)
