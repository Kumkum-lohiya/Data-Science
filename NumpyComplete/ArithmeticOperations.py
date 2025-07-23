import numpy as np
# var = np.array([1,2,3,4])
# varadd = var + 3
# print(varadd)
#
# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# varadd1 = var1 + var2
# varadd2 = np.add(var1,varadd)
# print(varadd1)
# print(varadd2)
#
# # 2D ARRAY
#
# var3 = np.array([[1,2,3,4],[1,2,3,4]])
# var4 = np.array([[1,2,3,4],[1,2,3,4]])
# varadd3 = np.add(var3,var4)
# print(var3)
# print(var4)
# print()
# print(varadd3)
#
# varreci = np.reciprocal(var3)
#
# print()
# print(varreci)

var = np.array([4,4,1,4,5,3,2])
print("min :",np.min(var),np.argmin(var))
print("max :",np.max(var),np.argmax(var))
print("sqrt :",np.sqrt(var))

var1 = np.array([[2,1,3],[9,5,6]])
print("minimum along column :",np.min(var1,axis=0))
print("minimum along row :",np.min(var1,axis=1))


var2 = np.array([1,2,3])
print(np.sin(var2))
print(np.cos(var2))
print(np.cumsum(var2))