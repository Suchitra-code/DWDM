import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print("The elements in a are:", a)
print("The elements in b are:", b)
print("Result after Addition:", a + b)
print("Result after Subtraction:", a - b)
print("Result after Multiplication:", a * b)
print("Result after Division:", a / b)
print("Result after increasing the number to the power of 4:", b ** 4)
print("Result after applying sin and multiplying with 10:", 10 * np.sin(a))
a[0] += 10
print("Result after adding first element with 10:", a)
print("Dot Product:", np.dot(a, b))
