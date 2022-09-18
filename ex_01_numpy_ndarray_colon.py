import numpy as np # Hat sich so eingebürgert dass als np importiert wird

am = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(am)
print(am[:,0])

am[:,0] = 1
am[am > 1] = 10
print (am)

am = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(am[am > 5])
i = np.where(am > 5)
print(i)
print(am[i])
am[i] = 20
print(am)