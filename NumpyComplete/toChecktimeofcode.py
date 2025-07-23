from timeit import timeit
import numpy as np

t1 = timeit(lambda: [j**4 for j in range(1, 9)], number=100000)

# NumPy vectorized version
t2 = timeit(lambda: np.arange(1, 9)**4, number=100000)

print(f"Pure Python time: {t1}")
print(f"NumPy time: {t2}")