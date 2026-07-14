import numpy as np
b = np.array([6, 4, 1, 3, 5, 9])
b[b < 4] = -1
print(b)
