import numpy as np
import pandas as pd
# ---------------------------------------------------------------
#   目录
#       生成数据
#       查看数据
#       选择
#       缺失值
#       运算-apply
#       合并
#       分组
#       重塑-reshape
#       数据透视表
#       时间序列
#       类别-Category
#       csv数据输入/输出
# --------------------------------------------------------------

s = pd.Series([1,3,5,np.nan,6,8])

# ---------------------------------------------------------------
#   生成数据
#   https://www.pypandas.cn/docs/getting_started/dsintro.html#series
# ---------------------------------------------------------------
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df2 = pd.DataFrame({'A':1.0,
                    'B':pd.Timestamp('20190102'),
                    'C':pd.Series(1,index=list(range(4)),dtype = 'float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})

# ---------------------------------------------------------------
#   查看数据
# ---------------------------------------------------------------
df2.to_numpy()
df2.describe()
df2.T  # 转置
df2.sort_index(axis=1,ascending=False)  # axis = 1>按照列排序,ascending> 升序
df2.sort_values(by='B',ascending=False)

# ---------------------------------------------------------------
#   选择数据-筛选
#   索引与选择数据：https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing
#   多层索引与高级索引：https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced
# ---------------------------------------------------------------
    # 按标签选择
df.A   #  等价 df['A']
df2[0:3]  #第0行到第3行
df.loc[dates[0]]
df.loc[:,['A','B']]  # df.loc['20130101':'20130103',['A','B']]
df.loc['20130101',['A','B']]
    # 按位置选择
df.iloc[0:3,1:2]  # 0-3行，1-2列
df.iloc[[1,2,4],[0,2]]
    # 布尔索引
df[df.A>0]   # 按行筛选
df[df>0]
    # isin 查找
df['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
df[df['E'].isin(['one','two'])]

# ---------------------------------------------------------------
#   赋值
# ---------------------------------------------------------------
    # 用索引自动对齐新增列的数据
s1 = pd.Series([1,2,3,4,5,6],index=pd.date_range('20190102',periods=6))
df['F'] = s1 # 长度和列一样
    # 按照标签赋值
df.at[dates[0],'A'] = 0 # 锁定一行数据
    # 用where条件赋值
df3 = df.copy()
# df[df>0] = -df3

# ---------------------------------------------------------------
#   缺失值
# ---------------------------------------------------------------
df.dropna(how='any')  # 删除有空行的行
df.fillna(value=5)
pd.isna(df)

# ---------------------------------------------------------------
#   运算
#   字符串：https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-string-methods
#   二进制操作： https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-binop
# ---------------------------------------------------------------
df.mean()   # 平均值，按照列
df.mean(1)  #平均值，按照行去组织

s1 = pd.Series([1,3,5,np.nan,6,8],index = dates).shift(2)  # shift按照纵轴方向移动
df.drop(['E','F'],axis=1,inplace=True)  # 删除两列
df.sub(s1, axis= 'index')

df.apply(np.cumsum)
# df.apply(lambda x : x.max()-x.min,axis=1)

# Series 可以调用str方法中的lower转换为小写办法  s1.str.lower()

# ---------------------------------------------------------------
#   合并
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging
# ---------------------------------------------------------------
    # Concat
cn1 = pd.DataFrame(np.random.randn(10,4))
pieces = [cn1[:3],cn1[3:7],cn1[7:]]
pd.concat(pieces)

    # Join
left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'],'rval':[4,6]})
pd.merge(left,right,on='key')

    # 追加
append = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
append1 = append.iloc[3]
append.append(append1,ignore_index=True)

# ---------------------------------------------------------------
#   分组  group by ,有三个步骤-分割、应用、组合
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby
#   分割：按条件把数据分割成多组
#   应用：为魅族单独应用函数
#   组合：将处理结果组合成一个数据结构
# ---------------------------------------------------------------
group = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foot'],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randn(8),
    'D':np.random.randn(8)
})
group_result = group.groupby(by=['A','B']).sum()

# ---------------------------------------------------------------
#   重塑
# ---------------------------------------------------------------
    # 堆叠
    # 可以看成是解压和压缩的区别，zip相当与压缩  zip（*）相当于解压。，生成元组对
stack_tuples = list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],
                          ['one','two','one','two','one','two','one','two']]))
index = pd.MultiIndex.from_tuples(tuples=stack_tuples,names=['first','second'])
df_stack = pd.DataFrame(np.random.randn(8,2),index = index,columns=['A','B'])
df_stack = df_stack[:4]
# 压缩后的 DataFrame 或 Series 具有多层索引， stack() 的逆操作是 unstack()，默认为拆叠最后一层
stacked = df_stack.stack()  # 将数据展示到一列上  unstack()是stack()的逆操作
stacked.unstack(1)  # 1是指的第几层索引

# ---------------------------------------------------------------
#   数据透视表  pivot_table
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-pivot
# ---------------------------------------------------------------
pivot_table_df = pd.DataFrame({
    'A':['one','one','two','three']*3,
    'B':['A','B','C']*4,
    'C':['foo','foo','foo','bar','bar','bar']*2,
    'D':np.random.randn(12),
    'E':np.random.randn(12)
})
pivot_table_df.pivot_table(index=['A','B'],columns='C')

# ---------------------------------------------------------------
#   时间序列  pivot_table
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries
# ---------------------------------------------------------------
    # freq = 'S' 时间格式：2019-01-01 00:00:04
    # freq = 'D' 时间格式：2019-01-01
    # freq参数： https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
rng = pd.date_range('1/1/2019',periods=100,freq='S')
ts = pd.Series(np.random.randint(0,500,len(rng)),index= rng)
    # 转换成其他时区
tz_rng = pd.date_range('1/1/2019',periods=5,freq='M')
ts_tz_rng = pd.Series(np.random.randn(len(tz_rng)),index = tz_rng)
    # ts_tz_rng.to_period()  将时间转换为 yyyy-mm格式
prng = pd.period_range('1991Q1','2000Q4',freq='Q-NOV')
ts_prng = pd.Series(np.random.randn(len(prng)),prng)
    # 频率转换  https://blog.csdn.net/bqw18744018044/article/details/80947243
ts_prng.index = (prng.asfreq('M','e')+1).asfreq('H','s')+9  # 切换1991Q1 -> 1991-03-01 09:00

# ---------------------------------------------------------------
#   类型Categories
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#categorical
#   https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html#api-arrays-categorical  -- api
# ---------------------------------------------------------------
cate_df = pd.DataFrame({
    'id':[1,2,3,4,5,6],
    'raw_grade':['a','b','b','a','a','e']
})
cate_df['grade'] = cate_df['raw_grade'].astype('category')
    # 重命名不同类型
cate_df['grade'].cat.categories = ['very good','good','very bad']

# ---------------------------------------------------------------
#   可视化文档
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization
# ---------------------------------------------------------------
ts_plot = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts_plot = ts_plot.cumsum()
ts_plot.plot()

# ---------------------------------------------------------------
#   CSV处理
#   https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-store-in-csv
# ---------------------------------------------------------------
#df2.to_csv('d:\\foo.csv')  # 存储到csv中
df2.to_excel('d:\\foo.xlsx','sheet1',index_col= None,na_values=['NA'])

# 错误 https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-compare
















