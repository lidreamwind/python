import numpy as np

'''
    矩阵乘法
'''
a = np.random.randint(0,10,size=(3,3))
b = np.random.randint(0,10,size=(3,4))

a.dot(b)
np.dot(a,b)

# @矩阵运算
print(a @ b)
