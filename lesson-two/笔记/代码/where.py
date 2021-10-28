import numpy as np

'''
    where函数
'''
nd1 = np.array([1,3,5,7,9])
nd2 = np.array([2,4,6,8,10])
cond = np.array([True,False,False,True,True])

print(np.where(cond,nd1,nd2))  # 条件如果是True则返回nd1中的数据，如果是False则返回nd2中的数据
a = np.random.randint(0,100,size=50)
print(np.where(a>50,a,-100)) #　大于５０则返回元数据，否则返回-100
np.where(a>50,a,a+20)

cond = (a>=60) & (a<70)
np.where(cond,a+10,a)

'''
    排序
'''
a = np.random.randint(0,20,size=10)
print(np.sort(a))  # 排序赋值给新数组
a.sort()  # 原数组排序
print(a)

index = a.argsort()
print(index) # 返回排序的索引
a[index]  # 花式索引



'''
    集合操作
'''
a = np.random.randint(0,30,size=15)
b = np.random.randint(0,30,size=15)

print(np.intersect1d(a,b)) #交集
print(np.union1d(a,b)) #并集
print(np.setdiff1d(a,b)) # 差集，a中有b中没有
