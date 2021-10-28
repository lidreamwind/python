import numpy as np

'''
    广播机制
'''
arr1 = np.array([0,1,2,3]*3)
arr1.sort()
arr1 =  arr1.reshape(4,3)
arr2 = np.array([1,2,3])
print(arr1,arr2)
print(arr1+arr2) # 广播，行不够，广播多行

arr3 =  np.array([[1],[2],[3],[4]])
print(arr1,'\n',arr3)
print(arr1+arr3)  # 列广播

## 三维
print("-------------------------------------3")
a = np.array([0,1,2,3,4,5,6,7]*3).reshape(2,3,4)
b = np.array([0,1,2,3,4,5,6,7]).reshape(4,2)

print(a)
print(b)
print(a+b)  # 三维广播