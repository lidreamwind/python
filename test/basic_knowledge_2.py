import numpy as np
import pandas as pd

index = pd.date_range('1/1/2000',periods=8)
s = pd.Series(np.random.randn(5),index = ['a','b','c','d','e'])
df = pd.DataFrame(np.random.randn(8,3),index = index,columns=['A','B','C'])
# -------------------------------------------------------------------------
#   目录：
#       属性和底层数据
#       加速操作
#       广播操作-加减乘除
#       缺失值与填充缺失值
#       比较操作
#       布尔简化----> df和Series的对比
#       描述性他统计 ----> 求和等函数
#       最大值与最小值对应的索引-离散化与分位数
#       函数应用
#       重置索引与更换标签-align--填充
#       迭代 for i in object
#       .dt 访问器 -访问时间的工具
#       排序
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
#   属性和底层数据
#   Pandas可以通过多个属性访问元数据：shape和轴标签。
#   推荐使用to_numpy
# -------------------------------------------------------------------------
df.columns = [x.lower() for x in df.columns]
    # .array用于提取数据
s.array  # pd.Series 转换为array数组
df_array = df.index.array
    # 提取Numpy数组，，s.to_numpy()  或者 np.asarray()
    # 推荐使用to_numpy
# s.to_numpy()  # 可以转换，可以转换类型
np_array = np.asarray(s)

# -------------------------------------------------------------------------
#   加速操作
#   借助numexpr与bolltleneck支持库，Pandas可以加速特定类型的二进制数值与布尔操作。默认启用状态
#   处理大数据加速效果明显，numexpr使用智能分块、缓存与多核技术；
#   bottleneck是一组专属cpython例程，处理nans值的数组时，特别快
#   https://pandas.pydata.org/pandas-docs/stable/install.html#install-recommended-dependencies
# -------------------------------------------------------------------------
# pd.set_option('compute.use_bottlenect',False)
# pd.set_option('compute.use_numexpr',False)

# -------------------------------------------------------------------------
#   广播操作-加减乘除
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sub.html
#   add(),sub(),mul(),div()，radd(),rsub()  加减乘除
# -------------------------------------------------------------------------
df_operator = pd.DataFrame({
    'one':pd.Series(np.random.randn(3),index=list('abc')),
    'two':pd.Series(np.random.randn(4),index=list('abcd')),
    'three':pd.Series(np.random.randn(3),index=list('bcd'))
})
row_operator = df_operator.iloc[1]
column_operator = df_operator['two']
df_operator.sub(row_operator,axis='columns')  # 相减

    #   多层索引，多层索引指定，需要按行处理，axis=0，level指定索引
dfmi_operator = df_operator.copy()
dfmi_operator.index = pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],names=['first','second'])
dfmi_operator.sub(column_operator,axis=0,level='second')
    # divmod  ，内置函数，，同时执行向下取整数与模运算  div,rem = divmod(s,[3])
    # 缺失值， df.add(df2,fill_value = 0)

# -------------------------------------------------------------------------
#   缺失值与填充缺失值
#   Series与DataFrame支持fill_value选项。
# -------------------------------------------------------------------------
# df.add(df2,fill_value=0)

# -------------------------------------------------------------------------
#   比较操作
#   Series与DataFrame支持eq、ne、lt、gt、le、ge
# -------------------------------------------------------------------------
# df.gt(df2)

# -------------------------------------------------------------------------
#   布尔简化
#   empty()  any()  all()   bool() 可以把数据汇总简化至单个布尔值
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.bool.html#pandas.DataFrame.bool
# -------------------------------------------------------------------------
(df>0).all() #  (df>0).any.any()
    #  比较对象是否有效
df + df == df+2  # Series与DataFrame等N为框架提供了 equals()方法。
(df+df).equals(df*2)
pd.Series(['foo','bar','gz']) == 'boo'  # => True,False,False
pd.Series(['foo','bar','gz']) == pd.Index(['boo','bar','qux'])  # => True,True,False

    # 合并重叠数据集
#   df1.combine_first(df2)

# -------------------------------------------------------------------------
#   描述性统计
#   sum()   mean()  quantile()  cumsum()    cumprod()
#   Series无需axis参数。 DataFrame index->axis =0  columns-> axis = 1
#   都支持，skipna关键字，指定是否要排除缺失数据
#   std() 标准差函数，ddo默认为1,
#   英文官网：https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#stats-moments-expanding-note
#   中文文档官网：https://www.pypandas.cn/docs/getting_started/basics.html#描述性统计
#   describe： https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-selectdtypes
# -------------------------------------------------------------------------
descrip_df  = df.sum(0,skipna = False)
ts_stand = (df - df.mean())/df.std(ddof = 0)

# -------------------------------------------------------------------------
#   最大值与最小值对应的索引-离散化与分位数
#   Series与DataFrame的idxmax()与idxmin()
#   Series的value_counts()方法可以统计值的数量
#   mode() 可以统计 Series和DataFrame的众数
#   cut()函数以值为根据实现分箱，离散化,将数值划分为多个区间  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html#pandas.cut
#   qcut() 计算样本分位数， https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.qcut.html#pandas.qcut
# -------------------------------------------------------------------------
s1 = pd.Series(np.random.randn(5))
s1.idxmin(axis=1),s1.idxmin(axis=0)

arr = np.random.randn(20)
factor = pd.cut(arr,4)
    # 结果如下：Categories (4, interval[float64]): [(-2.111, -1.153] < (-1.153, -0.2] < (-0.2, 0.754] < (0.754, 1.707]]
factor1 = pd.cut(arr,[-5,-1,0,1,5])
factor_qcut = pd.qcut(arr,4)
factor_qcut1 = pd.qcut(arr,[0,0.25,0.5,0.75,1])
    #  统计四分位数的个数
factor_qcut_count = pd.value_counts(factor_qcut1)

# -------------------------------------------------------------------------
#   函数应用
#   表级函数应用：pipe()    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe
#   行列级函数应用：apply()   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply
#   聚合Api：agg() 和 transform()  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg
#   元素级函数应用：applymap()  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.applymap.html#pandas.DataFrame.applymap
#   https://www.pypandas.cn/docs/getting_started/basics.html#函数应用
#   pipe 源码：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe
# -------------------------------------------------------------------------
    # windows API ：https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#stats-aggregate
    # resample API：https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-aggregate

    # agg操作
tsdf = pd.DataFrame(np.random.randn(10,3),columns=['A','B','C'],index=pd.date_range('1/1/2019',periods=10))
tsdf.iloc[3:7] = np.nan
def mymean(x):
    return x.mean()
tsdf_agg_sum = tsdf.agg(['sum','mean',lambda x:x.mean(),mymean])
tsdf_agg_dict = tsdf.agg({'A':['sum'],'B':[lambda x:x.sum()],'C':[mymean]})  # 字典是每列对应的，聚合
    # 创建自定义describe函数
from functools import  partial
q_25 = partial(pd.Series.quantile,q=0.25)
q_25.__name__ = '25%'
q_75 = partial(pd.Series.quantile,q=0.75)
q_75.__name__ = '75%'
tsdf_multi_function = tsdf.agg(['count','mean','std','min',q_25,'median',q_75,'max'])

    # transform操作,类型与对每个元素进行操作
tsdf_trans_abs = tsdf.transform('abs')  # tsdf_trans_abs.transfrom(np.abs)
tsdf_trans = tsdf.transform({'A':np.abs,'B':[lambda x:x+1]})

# -------------------------------------------------------------------------
#   重置索引与更换标签-对其对象-align--填充
#   reindex：1、让数据匹配一组新标签，并重新排序
#            2、无数据但有标签的位置插入缺失值
#            3、
#   reindex_like()：使用其他数据集的索引， df.reindex_like(df2)
#   align对其多个对象，和数据库的join很像： https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging
#       join选项有：outer、left、right、inner四个，连接方式
#       参数有：method、join、axis、limit(连续匹配的最大数量)、tolerance(限定了索引与索引器值之间的最大距离)
#       method的方法如下：
#           pad/ffill  向前填充
#           bfill/backfill 向后填充
#           nearest  从最近的索引值填充
#   drop():
#   rename():
# -------------------------------------------------------------------------
reindex_s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
reindex_st = reindex_s.reindex(['b','e','f','d'])
reindex_df = df.copy()
reindex_dfa = reindex_df.reindex(index=['c','f','b'],columns=['three','two','one'],)

    # align
align_s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
align_s1 = align_s[:4]
align_s2 = align_s[1:]
align_ss = align_s1.align(align_s2,join='inner')

    # rename
align_renmae = align_s.copy()
align_renmae.rename({'a':'one','b':'two'},axis=0,inplace=True)

# -------------------------------------------------------------------------
#   迭代 for i in object
#   基础迭代，for i in object 用于生成Series 值，或DataFrame 列标签
#   items()方法，通过键值迭代
#       for label，ser in df.items():
#   iterrows()，当做(index,Series)进行迭代
#       for index,row in df.iterrows():
#   itertuples，比iterrows快
#       for row in df.itertuples():
# -------------------------------------------------------------------------
for row in df.itertuples():
    a = row

# -------------------------------------------------------------------------
#   .dt 访问器 -访问时间的工具
#       day、hour、second、month、year
# -------------------------------------------------------------------------
dt_s = pd.Series(pd.date_range('20190101 09:10:12',periods=4))
dt_s.dt.second
dt_s[dt_s.dt.day == 2]

    # 格式化时间
dt_s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
    # 格式化时间字符串
dt_s.dt.strftime('%Y%m%d')   # 和strftime一样

# -------------------------------------------------------------------------
#   排序
#   排序所三种，按照索引排序、按照值排序、混合排序
#   nsmallest() nlargest() 最小值，最大值
#   Series: nsmalllest(5)  nlargest(2)
#   DataFrame: df.smallest(3,['a','b'])
# -------------------------------------------------------------------------
df.sort_index(ascending=False,axis=1)
align_renmae.sort_values(by=['one'])


