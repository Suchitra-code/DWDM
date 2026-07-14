import numpy as np
a = np.arange(12).reshape(4, 3) ** 2
print("The array is:\n", a)
print("The output of a[1:3] is:\n", a[1:3])
print("The output of a[1:3, 1:2] is:\n", a[1:3, 1:2])
print("The output of a[2,] is:", a[2,])
print("The output of a[:3,] is:\n", a[:3,])
print("The output of a[-1,] is:", a[-1,])
print("The output of a[-1, -1] is:", a[-1, -1])
