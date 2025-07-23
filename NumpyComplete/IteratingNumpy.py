import numpy as np;
var = np.array([9,8,7,6,5,4])
print(var)
print()
for i in var:
    print(i)
print()

#2D array
var1 = np.array([[1,2,3,4],[1,2,3,4]])
print(var1)
print()
for j in var1:
    print(j)

print()

for k in var1:
    for l in k:
        print(l)
print()

#3D array
var2 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(var2)
print(var2.ndim)
print()

for i in var2:
    for j in i:
        for k in j:
            print(k)

var3 = np.array([[[9,8,7,6],[1,2,3,4],[1,2,3,4]]])
print(var3)
print(var3.ndim)
print()
# change of datatype
for i in np.nditer(var3,flags=['buffered'],op_dtypes=["S"]):
    print(i)

for i in np.nditer(var3):
    print(i)

# data with index value
var4 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(var4)
# print(var4.ndim)
print()

for i,d in np.ndenumerate(var4):
    print(i,d)
