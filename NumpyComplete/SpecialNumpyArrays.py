import numpy as np

#ZEROS
ar_zero = np.zeros(4)
ar_zero1 = np.zeros((3,4))
print(ar_zero)
print()
print(ar_zero1)
print()

#ONES
ar_one = np.ones(4)
print(ar_one)

#EMPTY ARRAY

ar_em = np.empty(4)
print(ar_em) #empty array mai previously
             #given array ki value store ho jaati hai

#RANGE
ar_rn = np.arange(4)
print(ar_rn)

#DIAGONAL
ar_dia = np.eye(3)
print(ar_dia)

ar_dia1 = np.eye(3,5)
print(ar_dia1)

#LINSPACE
ar_lin = np.linspace(0,20,5)
print(ar_lin)



