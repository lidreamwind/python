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