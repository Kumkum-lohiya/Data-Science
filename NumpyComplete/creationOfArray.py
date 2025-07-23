#Array
import numpy as np
x = [1,2,3,4]
y = np.array(x)
print(y)


z = np.array([1,2,3,4])
print(z)
print(type(y))

l =[]
for i in range(1,5):
    int_1 = int(input("Enter any value : "))
    l.append(int_1)
print(np.array(l))