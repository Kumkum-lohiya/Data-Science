import numpy as np
ar1 = np.array([1,2,3,4])
print(ar1)
print("Dimension of array is ",ar1.ndim)

ar2 =np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print("Dimension of array is ",ar2.ndim)

ar3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(ar3)
print("Dimension of array is ",ar3.ndim)


#to create n dimension array
arn = np.array([1,2,3,4],ndmin = 10)
print(arn)
print("Dimension of array is ",arn.ndim)