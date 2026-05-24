import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1+arr2)

arr=np.array([1,2,3,4,5,6])
print(arr[0])
print(arr[-1])
print(arr[0:3])
print(arr[:2])

print(arr.shape)
print(arr.reshape(2,3))

print(arr+1)

m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6], [7,8]])
print(np.dot(m1, m2))

print(arr)
print(np.mean(arr))

print(np.std(arr))
print(np.random.rand(5))

arr=[1,2, np.nan, 5, 6]
print(arr)

print(np.isnan(arr))

import time
ls=list(range(100000000))
start=time.time()
print(start)
print(sum(ls))
end=time.time()
print(end)
print(end-start)

npls=np.array(ls)
start=time.time()
print(start)
print(np.sum(npls))
end=time.time()
print(end)
print(end-start)