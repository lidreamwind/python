import numpy as np

# 数组
nd1 = np.random.randint(0,10,size=5)
nd2 = np.random.randint(1,10,size=5)

print(nd1*nd2)
print(nd1-nd2)
print(nd1/nd2)
print(nd1+nd2)
#　幂运算　
print(nd1**nd2)
print(np.power(nd1,nd2))

print(np.log(100)) #自然底数e 2.718

# nd1对应位置的数据是否大于nd2中的数据
print(nd1>=nd2)

'''
    数字标量的运算
    -= , *= 
'''

'''
    复制和视图
'''
a = np.random.randint(0,10,5)
b = a
print(a,b)
print(a is b)

'''
    视图、查看或者浅拷贝
'''
a = np.random.randint(0,100,5)
b = a.view()
print(a)
print(b)
print(a is b)
print(a.flags.owndata)
print(b.flags.owndata)

'''
    深拷贝
'''
a = np.random.randint(-100,0,size=10)
b = a.copy()
print(a is b)
print(a.flags.owndata)
print(b.flags.owndata)


'''
    大数据量
'''
a = np.arange(1e8)
b = a[[1,3,5,7,9]]
del a


'''
    基本索引和切片
'''
a = np.random.randint(0,30,size=10)
print(a[3])  # 取一个
print(a[[1, 3, 5]])  # 取多个
print(a[0:3])  # 切片
print(a[:3])  # 冒号前不写，默认从0开始； 冒号后边不写，默认到最后一个元素
print(a[::2]) # 每两个取一个

b = np.random.randint(0,30,size=(10,10))

b[1] # 第一行
b[[0,3,5]] # 多行

b[1,1]
b[3,[2,4,6]] # 多为数组， 第四行数据获取多个元素

b[2::7,1::3]

'''
    花式索引和索引技巧
'''
a = np.arange(20)
b = a[3:7]  # 浅拷贝
b[0] = 1024
print(a," ----- ",b)

a = np.arange(20)
b = a[[3,4,5,6]] # 花式索引 ,返回的是深拷贝的值
print(a,b)

a = np.random.randint(0,151,size=(100,3))
cond = a>=120 #逻辑运算  只要大于120就返回
# boolean  True=1 False=0
#　三门科目的条件相乘，三个科目都是120以上的
cond2 = cond[:,0]*cond[:,1]*cond[:,2]
print(a[cond2])

# 大于等于120，小于等于30找到
cond1 = a>=120
cond2 = a<=30
print(a[cond2[:, 0] * cond2[:, 1] * cond2[:, 2]])


