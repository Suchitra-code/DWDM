import numpy as np
x = np.array([1, 2, 3])
print("The elements in X before deleting:", x)
newarray = np.delete(x, 2)
print("The elements in X after deleting:", newarray)
