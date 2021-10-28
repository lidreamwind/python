import numpy as np

'''
    数据转置
'''
a = np.random.randint(0,10,size=(3,5))
a.reshape(5,3) # 变成 五行三列
a.reshape(15,1,1)
a.reshape(-1,3) #  自动整型，-1表示数据

print(a.T)  # 转置，行变列， 列变行
np.transpose(a,(1,0)) #  行 0，列1，默认情况下（0,1）---->调整为1,0

print("-------------------------------")
b = np.random.randint(0,10,size=(3,5,7))
print(b)
print(np.transpose(b,(2,1,0)))  # 调整维度结构，将2,0维度数据对调

'''
    数据堆叠
'''
print("================================")
nd1 = np.random.randint(0,10,size=(3,5))
nd2 = np.random.randint(0,10,size=(3,5))
print(np.concatenate([nd1, nd2])) # 默认行增加
print(np.concatenate([nd1, nd2],axis= 1 )) # 列增加

print(np.hstack((nd1,nd2)))  # 堆叠,水平，列增多
print(np.vstack((nd1,nd2)))  # 堆叠，行


'''
    数据拆分
'''
print("-----------------------------------------------")
a = np.random.randint(0,100,size=(15,10))
print(np.split(a,indices_or_sections=3)) # 给数字，平均分成多少份
print(np.split(a,indices_or_sections=2,axis=1))  # 列被平均分成两份
print(np.split(a,indices_or_sections=[1,5,9]))  # 0-1,1-5,5-9,9- 分隔，参数给列表，根据列表中的索引切片

print(np.hsplit(a,indices_or_sections=2))
print(np.vsplit(a,indices_or_sections=5))

