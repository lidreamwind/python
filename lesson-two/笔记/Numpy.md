# Numpy基础

## 作用

- 存储和处理大型矩阵，比python自身的嵌套列表要搞笑
- 支持大量的维度数组与矩阵运算
- 提供了大量的数学函数库，**包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅里叶变换、基本线性代数、基本统计运算和随机模拟**



几乎所有从事Python工作的数据分析师都利用NumPy的强大功能。

- 强大的N维数组
- 成熟的广播功能
- 用于整合C/C++和Fortran代码的工具包
- NumPy提供了全面的数学功能、随机数生成器和线性代数功能



**安装Python库**

1. pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple
2. pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple



**启动终端**
Windows----> 快捷键：win + R ----->输入：cmd回车------>命令行出来
Mac ---->启动终端

**启动jupyter**
进入终端输入指令:jupyter notebook
在哪里启动jupyter启动，浏览器上的目录，对应哪里

## 数组创建



```markdown
import numpy as np

# 可以将python中list列表转换为Numpy数组
l = [1,2,3,4]

# Numpy数组
ndl = np.array(l) # 输入一部分，可以使用tab不全
print(ndl)
display(ndl)  # 显示
#output：
[1 2 3 4]
array([1, 2, 3, 4])


nd2 = np.zeros(shape=(3,4),dtype=np.int16) # shift+tab提示方法的属性，
nd2
#output：
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]], dtype=int16)

nd3 = np.ones(shape=(3,4),dtype=np.float32)
nd3
# output
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]], dtype=float32)

np.full(shape=(3,4,5),fill_value=3.1415926) # 生成任意指定的数据

nd5 = np.random.randint(0,100,size=20) # 从0到100生成随机数字，int，整数
nd5

nd6 = np.random.rand(3,5) # 生成0-1之间的随机数

nd7 = np.random.randn(3,5) # 正泰分布，平均值是0，标准差是1
nd8 = np.random.normal(loc=175,scale = 10,size=(3,5)) # 正态分布，平均值是175，标准差是10

nd9 = np.arange(1,100,step=10) # 等差数列,,左闭右开
nd10 = np.linspace(0,99,100) # 等差数列 ， 左闭右闭，，100代表生成等差数列的长度
```

## Jupyter插件

jupyter扩展插件

1. pip install jupyter_contrib_nbextensions -i https://pypi.tuna.tsinghua.edu.cn/simple
2. pip install jupyter_nbextensions_configurator -i https://pypi.tuna.tsinghua.edu.cn/simple

jupyter contrib nbextension install --user

jupyter nbextensions_configurator enable --user





## 复制和视图

````python
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
````



## 索引和切片

```python
'''
    基本索引和切片
'''
a = np.random.randint(0,30,size=10)
print(a[3])  # 取一个
print(a[[1, 3, 5]])  # 取多个
print(a[0:3])  # 切片
print(a[:3])  # 冒号前不写，默认从0开始； 冒号后边不写，默认到最后一个元素
print(a[::2]) # 每两个取一个
print(a[::-1]) # 倒序输出
print(a[6::-2]) # 从第七个元素开始倒序


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
```

# Numpy高级应用

## 形状操作

```python
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


```



## 广播操作

````python
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
````



## 通用函数

![image-20211025222407010](.\图片\numpy-function.jpeg)

```python
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
```



## 排序-where

```python
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
```



## 数学统计函数

![image-20211026210858743](.\图片\math-functions.jpeg)

```python
import numpy as np
a = np.random.randint(0,100,size=(3,5))
print(a)
print('-----------------')

print(a.min(),a.min(axis=0),a.min(axis=1)) # 最小
print(a.max(),a.max(axis=0),a.max(axis=1)) #　最大
print(a.mean())  # 平均数
print(np.median(a)) # 中位数
print(a.sum())  # 求和
print(a.std())  # 标准差
print(a.var())  # 方差，数据内部的波动情况
print(a.cumsum())  # 累加和
print(a.cumprod()) # 累乘和
print(a.argmax())  # 最大值索引
print(a.argmin())  # 最大值索引
print(np.argwhere(a>60))  # 大于50的索引

# 协方差（属性之间进行计算），方差概念类似（数据内部，属性内部计算）
np.cov(a)

# 相关性系数,根据协方差计算而来， 1正相关， -1 负相关，，0不相关
np.corrcoef(a)
```



## 矩阵乘法

点乘

![image-20211027212630378](.\图片\机器学习.jpeg)

```python
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

```

