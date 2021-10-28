import numpy as np

a = np.array([-1,-3,-5,-7,1,4,2,9])
b = np.random.randint(1,20,size=8)
print(a)
print(b)

print(np.abs(a))  # 绝对值
print(np.sqrt(b))  # 开平方
print(np.square(a))  # 平方
print(np.exp(2))  # 自然底数e的多少次幂
print(np.log(20.085536)) # 自然底数e对数求解
print(np.sin(np.pi/2))  # 90度的正弦值
print(np.cos(np.pi/2))  # 90度的余弦值
print(np.tan(np.pi/6))  # 30度的正切值
print(np.maximum(a,b))  # a和b中求大的拿一个
print(np.minimum(a,b))  # a和b中求小的拿一个。买的。

nd1 = np.array([1,3,0,4])
nd2 = np.array([-1,-3,4,8])
print(nd1.any())   # 只要有一个是true就是true
print(nd1.all()) # 所有True，返回True

print(np.inner(nd1,nd2))  # 返回向量内积

nd1 = np.random.randint(0,100,size=30)
print(np.clip(nd1,10,80))  # 将小于10和大于80的裁减掉

nd2 = np.random.randn(20)
print(nd2.round(2)) # 保留两位小数

print(np.ceil(2.7)) # 向上取整
print(np.floor(2.7)) # 向下取整

a = np.random.randint(0,10,size=(3,3))
print(np.trace())  #  计算对角线上的和