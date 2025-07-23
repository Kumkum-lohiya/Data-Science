import numpy as np
var = np.array([1,2,3,4])
var1 = np.array([9,8,7,6])

ar = np.concat((var,var1))
print(ar)
print()


#2D ARRAY
vr= np.array([[1,2],[3,4]])
vr1 = np.array([[9,8],[7,6]])
print(vr)
print()
print(vr1)
print()
arr = np.concat((vr,vr1),axis=1)
arr1 = np.concat((vr,vr1),axis=0)
print(arr)
print(arr1)
print()

#Array merging using stack function
var_1= np.array([1,2,3,4])
var_2 = np.array([9,8,7,6])
print(var_1)
print(var_2)
print()
ar_1= np.hstack((var_1,var_2)) # along horizontal row
ar_2= np.vstack((var_1,var_2)) # along vertical column
ar_3= np.dstack((var_1,var_2)) # along height
print(ar_1)
print(ar_2)
print(ar_3)
print()