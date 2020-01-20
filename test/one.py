import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql
source = pymysql.connect(host='192.168.142.130',port=3306,user='root',passwd='123456',db='tempdb',use_unicode=True,charset='UTF8MB4')
target_engine = create_engine('mysql+pymysql://root:123456@192.168.142.130/test?charset=utf8')

# 操作code表
sql = 'select * from code'
result = pd.read_sql_query(sql=sql,con = source)

# 筛选所需字段，并按照科目编码升序排列，两种写法
# new = result[['cclass','ccode','ccode_name','igrade','cbook_type']].where(result['igrade']>0).sort_values('ccode',axis=0,ascending=True)
new = result.loc[result['igrade']>0,['cclass','ccode','ccode_name','igrade','cbook_type']].sort_values('ccode',axis=0,ascending=True)
new['bookcode'] = '1002'
new['bookname'] = '测试数据'

#存储数据到MySQL-test库中
# pd.DataFrame(new).to_sql(name='code',con=target_engine,if_exists='append',schema='test',index=False)

# 操作凭证表
voucher_sql = 'select * from gl_accvouch'
voucher = pd.read_sql(sql=voucher_sql,con=source)
voucher_new = voucher[['i_id','iperiod','ino_id','dbill_date','cbill','cdigest','ccode','md','mc','ccode_equal','ccus_id','cdept_id','citem_id','citem_class']]

#设置值
voucher_new['ccus_id'] = np.random.randint(1,10000,voucher_new.__len__())   # 客户
voucher_new['cdept_id'] = np.random.randint(1, 10, voucher_new.__len__())        # 部门

fitem = pd.DataFrame([[98,97,96,95,94],['让自己知道','一二三四','生命无常','资产负载','现金流量']])
index = np.random.randint(0,5,voucher_new.__len__())

voucher_new['citem_id'] = [fitem[x][0] for x in index]
voucher_new['citem_class'] = [fitem[x][1] for x in index]

#  对5取余为0的，设置为空  ---暂定,  构造假数据
voucher_new['ccus_id'] = [voucher_new.loc[x]['ccus_id'] if x%5>2 else np.nan  for x in voucher_new.index]   # 3 和 4
voucher_new['ccus_id'] = [np.nan if x%5==3 else voucher_new.loc[x]['ccus_id']  for x in voucher_new.index]
voucher_new['cdept_id'] = [voucher_new.loc[x]['cdept_id'] if x%5==2 else np.nan for x in voucher_new.index]
voucher_new['citem_id'] = [voucher_new.loc[x]['citem_id'] if x%5<2 else np.nan for x in voucher_new.index]
voucher_new['citem_class'] = [voucher_new.loc[x]['citem_class'] if x%5<2 else np.nan for x in voucher_new.index]

#  row_number() over(partition by id order by id)  的实现
    #  groupby两列是为了唯一锁定一个凭证
voucher_new['number'] = voucher_new['i_id'].groupby([voucher_new['ino_id'],voucher_new['iperiod']]).rank(ascending=True,method='dense')

# cus = voucher_new[voucher_new['ccus_id'].map(lambda x:x>0)]['ccus_id','id'].copy()   # 查找不为空的数据

# 索引号拿出来作为一列
voucher_new['id'] = voucher_new.index
# 重命名
voucher_new.rename(columns = {'ino_id':'pzbh','i_id':'pzxh'},inplace=True)
voucher_new.shift(1)

#



print(voucher_new)