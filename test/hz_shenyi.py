import re
import numpy as np
import pandas as pd

# pandas 操作SQL https://blog.csdn.net/duxu24/article/details/53469781

    # 设置列宽
pd.set_option('display.max_colwidth',80)
pd.set_option('display.width', 180)  # 150，设置打印宽度​
pd.set_option('display.max_rows', None) # 打印最大行数
pd.set_option('display.max_columns', 40) # 打印最大列数
#列名和内容对其
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 设置numpy浮点数数值  https://blog.csdn.net/weixin_40309268/article/details/83579381
np.set_printoptions(precision=4, threshold=8, edgeitems=4, linewidth=75, suppress=True, nanstr='nan', infstr='inf')
#  设置pandas浮点数   https://blog.csdn.net/LuCh1Monster/article/details/100011189
pd.set_option('float_format', lambda x: '%.2f' % x)

#  处理余额表
    #  usecols指的是引用第几列  header指的是标题行    skiprows指的是跳过多少行
kmye = pd.read_excel('d:\\kmye.xlsx',sheet_name='Sheet1',header=None,skiprows=2)

    # 增加列名
kmye.columns = ['kmbh','kmmc','kmfx','bz','qcye','jffse','dffse','qmye']

    # 过滤科目表中Person等开头的辅助项目，保留科目余额数据

        # 包含-
        # 长度<4
        # 全是字母
        # 以1-9数字开头
def kmfzgl(row):
    x = row['kmbh']
    regex = re.compile('^[a-z]+')  # 过滤所有科目编号是字母的情况
    regex1 = re.compile('^[1-9]+') # 判定所有是以1-9开头的
    # 科目筛选规则，长度大于3， 首字母是以1开头，，，且没有字母
    if(len(x)>3 and len(regex.findall(x.lower()))<1 and len(regex1.findall(x))>=1):
        if (x.__contains__('-')):
            return row
        else:
            row['is_fz'] = 1  # 科目余额标记为1
            return row
    return row

    #定义通道函数，用于处理整个DataFrame
def subject_deal(df):
    kmye = df.apply(kmfzgl,axis=1)  # 调用kmfzgl，处理行，增加标识
    return kmye # 筛选科目

    # 增加列标识，标注科目信息
kmye['is_fz'] = 0 # 0代表是辅助项目，1代表不是辅助项目
kmye = kmye.pipe(subject_deal)  # 用于获取标准的会计科目余额  以及 标记辅助项目
kmye_new = kmye.where(kmye['is_fz']>0).dropna(axis=0,how='all')  # 标准的科目余额

# 将空值给换成0，用于计算
kmye['qcye'] = kmye_new['qcye'].fillna(value=0)
kmye_new['jffse'].fillna(value=0,inplace=True)
kmye_new['dffse'].fillna(value=0,inplace=True)
kmye_new['qmye'].fillna(value=0,inplace=True)

    # 加载凭证
pz = pd.read_excel('d:\\pz.xlsx',sheet_name=0,header=0,parse_dates=True)
    # 重命名列名
pz.rename({'凭证日期':'pzrq','类型':'pzlx','编号':'pzbh','科目名称':'kmmc','摘要':'zy',
           '借方':'jfje','贷方':'dfje','核算项目':'fzbh','对方科目':'dfkm'},inplace=True,axis=1)

    # 补充空缺的凭证日期，类型，编号
pz_new = pz.fillna(method='ffill').fillna(method='bfill')  # 先向前填充，然后向后填充
pz_new['pzbh'] = pz_new['pzbh'].astype('int')  # 将凭证编号转换为int类型
pz_new['pzrq'] = pz_new['pzrq'].astype('int')  # 将凭证日期转换为int类型，为了能够将其格式化

    # 定义函数，将时间进行格式化，并将结果返回
def format_pzrq(sq):
    pzrq = str(sq)
    if(len(pzrq)>6):
        return pzrq.replace('-','')[:6]
    return pzrq
    # 增加新的一列，为年月 201701
pz_new['ymonth'] = pz_new.pzrq.map(format_pzrq)
# pz_new['ymonth'] = pd.to_datetime(pz_new['pzrq'],format='%Y%m%d')  #创建新列，格式化时间为年月20150102 ---补充

    # 根据凭证日期和科目名称进行分组求和，用于和科目余额进行join，以进行累计计算
    # reset_index()是为了将索引值设为列
    # 本期发生额
pz_new_sum = pz_new[['ymonth','kmmc','jfje','dfje']].groupby(by=['ymonth','kmmc']).sum().reset_index()

    # 将 kmye_new 和 pz_new_sum 通过科目名称关联起来
kmye_pz = pd.merge(left=kmye_new,right=pz_new_sum,left_on='kmmc',right_on='kmmc').reset_index()
    # 根据科目编号求jfje的累计发生额和贷方金额的累计发生额。
    # 前提是ymonth已经升序排列,其中索引值便是kmye的下标
    # 累计发生额
jfje_cumsum = kmye_pz.groupby(by=['kmbh'])['jfje','dfje'].cumsum().reset_index()  # 此部分可以在pz_new_sum中做计算
kmye_pz_new = pd.merge(left=kmye_pz,right=jfje_cumsum,how="left",on='index')

    # qcye,jffse,dffse,qmye 都是object类型，且含有逗号，，对他进行标准的float格式化
format_float = lambda row:str(row).replace(',','')
kmye_pz_new['qcye'] = kmye_pz_new['qcye'].map(format_float).astype('float')
kmye_pz_new['jffse'] = kmye_pz_new['jffse'].apply(format_float).astype('float')  # 格式化数据格式为
kmye_pz_new['dffse'] = kmye_pz_new['dffse'].apply(format_float).astype('float')
kmye_pz_new['qmye'] = kmye_pz_new['qmye'].map(format_float).astype('float')

    # 本期发生额,jfje_x,dfje_x  累计发生额 jfje_y,dfje_y，，使用会计公式得到结果
    # 期末金额
kmye_pz_new['qmye'] = kmye_pz_new['qmye'].add(kmye_pz_new['jfje_y'],fill_value=0,axis=0).sub(kmye_pz_new['dfje_y'],fill_value=0,axis=0)
    # 期初金额
kmye_pz_new['qcye'] = kmye_pz_new['qcye'].add(kmye_pz_new['jfje_x'],fill_value=0,axis=0).sub(kmye_pz_new['dfje_x'],fill_value=0,axis=0)
    # 重命名字段
kmye_pz_new.drop(['jffse','dffse','index'],axis=1,inplace=True)  #  先删除列
kmye_pz_new.rename({'jfje_x':'bqjffse','dfje_x':'bqdffse','jfje_y':'bqljjffse','dfje_y':'bqljdffse'},inplace=True,axis=1)

    # 余额表
balance = kmye_pz_new.copy()

#---------------------------------------------
#   方法二实现期初余额的计算，，平移法 shift
#---------------------------------------------
r = kmye_pz_new.copy()
r['col'] = r.qmye.shift(periods=1,fill_value=0,axis=0)  # 向下移动一个单位

    #  定义函数移动范围
def move_qcye(row):
    if(row['ymonth'][4:6]>'01' and row['ymonth'][4:6]<='12'):
        row['qcye'] = row['col']
    return row
r.qcye = 0
    # 期末余额移动到下一个月期初
    #  apply 的函数，必须有返回值，才行
balance_1 = r.apply(move_qcye,axis=1)  # axis =0 代指的是一列，，axis=1指的是一行

    # 提取科目
subject = kmye_new[['kmbh', 'kmmc']].drop_duplicates().sort_values(by='kmbh')
subject['kmbh'].astype('object')

    # 定义函数判断科目级次和父级科目代码
def grade_fathercode(row):
    kmbh = row['kmbh']
    if(len(kmbh)==4):
        row['grade'] = 1
        row['f_code'] = '0000'
    else:
        row['grade'] = (len(kmbh)-4)/2 + 1
        row['f_code'] = kmbh[:len(kmbh)-2]
    return row

subject_new = subject.apply(grade_fathercode,axis=1)

    # pipe 管道方法案例
def pipe_f(df):
    return df.apply(grade_fathercode,axis=1)
# s.pipe(pipe_f)
pz.drop_duplicates()
    # 科目12月份进行匹配，得到基准余额表项
def get_km_subject(df):
    month = pd.DataFrame({'ymonth':balance['ymonth'].drop_duplicates(),'r':1}) # 获取月份，r用于做笛卡尔积
    su = df.assign(r=1) # 增加列做笛卡尔积
    # 将科目进行join,按照每个月份都得到一个科目
    temp = pd.merge(left=month,right=su,on='r').sort_values(by=['kmbh','ymonth'],ascending=[True,True])
    return pd.merge(left=temp,right=balance,left_on=['kmbh','ymonth'],right_on=['kmbh','ymonth'],how='left')

    # 获取 余额表基本科目项
km_subject = subject_new.pipe(get_km_subject)
km_subject.loc['qcye':'bqljdffse'].fillna(value=0,inplace=True)

    # 定义函数，用于更新新的列值
def cacute_fcode(row):
    if(row['qm']>0):
        row['qcye'] = row['qc']
        row['qmye'] = row['qm']
        row['bqjffse'] = row['bqjfse']
        row['bqdffse'] = row['bqdfse']
        row['bqljjffse'] = row['bqljfse']
        row['bqljdffse'] = row['bqldfse']
    return row

    # 定义函数计算余额表
def caculate_balance_father(df):
    df['grade']= df['grade'].astype('int')
    max_grade = df['grade'].max()
    #  删除无用列
    df.drop(['r', 'bz'], inplace=True, axis=1)  # 默认行，axis=1删除列
    # 科目总共有3级，从第三级，一级一级向上算,修改父级科目值
    for month in range(max_grade-1):
        # 按照科目等级逐级向上汇总
        # 获取科目等级累加信息
        temp = df.where(df['grade']==max_grade-month).groupby(['ymonth','f_code'])['qcye','qmye','bqjffse','bqdffse','bqljjffse','bqljdffse',].sum().reset_index()
        # 重命名列，防止列名重复
        temp.rename({'ymonth':'month','f_code':'fcode','qcye':'qc','qmye':'qm','bqjffse':'bqjfse','bqdffse':'bqdfse',
                     'bqljjffse':'bqljfse','bqljdffse':'bqldfse'},axis=1,inplace=True)
        #  结果集join在一起
        result = pd.merge(left=df,right=temp,left_on=['kmbh','ymonth'],right_on=['fcode','month'],how='left')

        # 结果赋值
        result = result.apply(cacute_fcode,axis = 1)

        # 删除无用列
        result.drop(['month','fcode','qc','qm','bqjfse','bqdfse','bqljfse','bqldfse'],axis=1,inplace=True)

        # 变更df的值
        df = result.copy()
    return df
    #   计算balance的值,,最终余额表的值
balance_new = km_subject.pipe(caculate_balance_father).sort_values(by=['ymonth','kmbh'],ascending=[True,True])
balance_new.fillna(value=0,inplace=True)

#---------------------------------------------
#----------------  辅助帐部分   ---------------
#---------------------------------------------
fzbh_items_pz = pz[['fzbh']][-pz['fzbh'].isna()].drop_duplicates().reset_index()
fzbh_items_pz.rename({'index':'kmbh','fzbh':'kmmc'},inplace=True,axis=1)
fzbh_items_pz['lx']='pz'  # 增加类型列

    # kmye已经进行了标记，，要带出辅助账的科目信息，用于计算辅助账属于哪一科目
    # kmye已经对is_fz进行了标记，科目是1，辅助账是0，按照is_fz进行累加，当累加值为1的时候，是辅助账对应的科目
kmye_fz_index = kmye['is_fz'].diff(periods=-1).reset_index()  # 获取辅助科目出现的位置
kmye.reset_index(inplace=True)  # 索引值作为列出现
kmye_fz_subject = pd.merge(left=kmye_fz_index,right=kmye,how='inner',on='index')

    # 赋值is_fz_x
def gurantee_fz_subject(row):
    if(row['is_fz_x']==1):
        row['is_fz_y'] =0
    return row
km_fz_temp = kmye_fz_subject.apply(gurantee_fz_subject,axis=1)
    # 不能去重，为了以后的计算辅助科目余额
fzbh_items_balance = km_fz_temp.where(km_fz_temp['is_fz_y']<1).dropna(axis=0,how='all')[['kmbh','kmmc']]
fzbh_items_balance['lx'] = 'balance'

    # 将凭证和余额的辅助账信息合并在一起，进行统计
fzbh_list = [fzbh_items_pz,fzbh_items_balance]
fzbh_items_result = pd.concat(fzbh_list,axis=0,sort=True)

# 通过pipe管道，将df传入，然后生成dataframe,Dataframe 记录类型
    # 定义函数，用来解析数据：【部门辅助账：市场销售部】 【个人往来辅助账：市场销售部-冯真奇】
    # 按照【】 ； - 依次分割数据，遍历循环得到结果
    # 处理凭证的辅助账项目
def format_fz(fzmc,fzbh,df):   # str是要解析的字符串， index是解析的字符串对应的编号
    fzname = fzmc.split(' ')
    for cell in fzname: # 循环有几个【】括起来的部分
        grade = 1  # 辅助帐级次判定
        type = ''  # 辅助帐类型，用于查找对应的辅助帐，取的是冒号前面的部分
        for x in cell.replace('【','').replace('】','').split('：'):  # 【】中通过：号分割数据
            if(len(x)<1): # 若为空，，那么跳过
                continue
            if(grade == 1): # 第一个等级
                type = x # 辅助帐类型
                df_type = df[df['type'].isin([type])]  # 用于判断此类型是否存在
                # {'fzbh':str(fzbh)+'-'+str(grade),'fzmc':x,'father':'0000','grade':grade}
                # 判断有无存在，若不存在，，则直接插入，，否则，，  df_result[df_result['fzmc'].isin(['部门辅助账'])]
                if(df_type.size<1):  # 不存在
                    df = df.append({'fzbh':str(fzbh)+'-'+str(grade),'fzmc':x,'father':'0000','grade':grade,'type':type},ignore_index=True)
            else:  # r若不是第一层级，则进行切分，按照-  grade>=2
                 # 父亲编号，ffzbh
                ffzbh = ''
                rs = x.split('-')
                for xs in rs:   # 按照层级来划分,如：市场销售部-冯真奇
                    df_type = df[df['fzmc'].isin([xs]) & df['type'].isin([type])] # 判断此类型是否存在
                    if(df_type.size>0): # 若存在当前子类型，则跳过.拿到父级编号后跳过
                        # 处理['【部门辅助账：市场销售部】', '【个人往来辅助账：市场销售部-市场销售部】'] 情况
                        if(df[df['all_name'].isin([cell])].size<1):  # 不是最后一级，，就赋值，判断all_name是否存在
                            if(len(rs)>grade-1):  # 是否是末级，末级不在记录父级编号
                                ffzbh = df_type['fzbh'].max()
                                grade +=1 # 循环终止前要执行
                                continue # 调出循环，，
                        else:
                            continue
                    df_type = df[df['type'].isin([type])]  # 获取一级类型的所有数据
                    fb = df_type['fzbh'].to_numpy()[-1]  # 最大编号,max默认比较的是字符串，转为数组，去最后一个即可
                    bcbh = fb.split('-')[0] + '-' + str(int(fb.split('-')[1]) + 1)  # 本次辅助编号
                    if (grade == 2):  # 辅助编号是父级,后一级次
                        ffzbh = df_type['fzbh'].min()

                    if(len(rs)>grade-1): # 有对应辅助帐 ,且不在最后一个级次，非末级，不增加all_name
                        df = df.append({'fzbh':bcbh,'fzmc':xs,'father':ffzbh,'grade':grade,'type':type},ignore_index=True)
                        ffzbh = bcbh # 非末级，的父级科目
                    elif(len(rs)==grade-1):  # 在最后一个级次，，插入辅助帐信息，用来更新辅助帐信息
                        df = df.append({'fzbh': bcbh, 'fzmc': xs, 'father': ffzbh, 'grade': grade, 'type': type,'all_name':cell},ignore_index=True)
                    grade += 1 # 记录等级
            grade += 1
    return df

# 处理余额表辅助账情况

    # fzbh_items_result得到的余额表中，是科目带有辅助项目，按以下步骤：
    # 判断是否是科目，若是科目跳过本次循环
    # 若不是科目，按照级次进行处理
def format_balance(fzmc,fzbh,df,fztypecode,fztypename):
    # 父级编号和名称，一级
    fztypebh = fztypecode
    # df_result_balance = pd.DataFrame(data=None, columns=['fzbh', 'fzmc', 'father', 'grade', 'type', 'all_name'])
    regex = re.compile('^[A-Za-z]+$') # 正则匹配是否全部为字母
    grade = 1  #  辅助项目等
    # 若全部为字母，则为第一大类
    if( len(regex.findall(fzbh))>0 ):  # 说明是字母，则是分类
        type = fzmc
        df_type = df[df['fzmc'].isin([fzmc.replace(' ','')])]
        if (df_type.size < 1):
            df = df.append({'fzbh': fzbh, 'fzmc': fzmc, 'father': '0000', 'grade': grade, 'type': type},ignore_index=True)
            fztypecode = fzbh
            fztypename = fzmc
        else:
            fztypecode = df_type[df['grade'].isin([grade])]['fzbh'].max()
            fztypename = df_type[df['grade'].isin([grade])]['fzmc'].max()
    else:
        # 类别等级是1，那么子类别则等级是2开始，，故而，，grade先加1
        if(grade<2):
            grade += 1
        if(fzbh.__contains__('-')):  # 辅助编号和辅助名称列表是一一对应的关系
            fzbh_list = fzbh.split('-')  # 辅助编号列表
            fzmc_list = fzmc.split('-')  # 辅助名称列表
            for fzbh_temp,fzmc_temp in zip(fzbh_list,fzmc_list):
                # 判断是否重复
                df_type = df[df['fzmc'].isin([fzmc_temp]) & df['type'].isin([fztypename])]
                if(df_type.size>0):  # 若存在则跳过
                    if (df[df['all_name'].isin([fzmc])].size < 1):  # 不是最后一级，，就赋值，判断all_name是否存在
                        if (len(fzmc_list) > grade - 1):  # 是否是末级，末级不在记录父级编号
                            fztypebh = df_type[df['grade'].isin([grade])]['fzbh'].max()
                            grade += 1  # 循环终止前要执行
                            continue  # 调出循环，，
                    else:
                        continue
                # 插入数据
                if(len(fzmc_list) ==grade-1): # 最后一个等级
                    df = df.append({'fzbh': fzbh_temp, 'fzmc': fzmc_temp, 'father': fztypebh, 'grade': grade, 'type': fztypename,'all_name':fzmc},ignore_index=True)
                else:
                    df = df.append({'fzbh': fzbh_temp, 'fzmc': fzmc_temp, 'father': fztypebh, 'grade': grade, 'type': fztypename},ignore_index=True)
                    fztypebh = fzbh_temp
                grade += 1

        else:
            # 判断是否重复
            df_type = df[df['fzmc'].isin([fzmc]) & df['type'].isin([fztypename])]
            if (df_type.size < 1):  # 若存在则跳过
                df = df.append({'fzbh': fzbh, 'fzmc': fzmc, 'father': fztypebh, 'grade': grade, 'type': fztypename,'all_name':fzmc},ignore_index=True)
    return fztypecode,fztypename,df



#主函数方法体，辅助项目，凭证和余额
def pipe_fz_item(df):
    # 创建辅助项目等级表，按照如下方式存放,fzbh 是辅助编号，fzmc是名称，father是父级代码，grade是级次，type是类型,type2是来自pz还是balance
    df_result = pd.DataFrame(data=None, columns=['fzbh', 'fzmc', 'father', 'grade','type','all_name'])

    fcode = ''
    fname = ''

    # 遍历循环dataframe的所有数据，逐步分析得到辅助账信息
    for item in df.itertuples():
        if(item.lx=='pz'): # 凭证的辅助项目的处理
            df_result = format_fz(str(item.kmmc),str(item.kmbh),df_result)  # 处理辅助内容，得到小的dataframe
        else:  # 余额表辅助项目的处理
            # 判断是否科目，不是科目之执行，否则跳过
            if(balance[balance['kmbh'].isin([str(item.kmbh)])].size<1):
                fcode,fname,df_result = format_balance(str(item.kmmc),str(item.kmbh),df_result,fcode,fname)
    return df_result

# 获取辅助账辅助结构
# fz_i = fzbh_items_balance.pipe(pipe_fz_item)
fz_item = fzbh_items_result.pipe(pipe_fz_item)

# 获取balance_item数据
balance_item_temp = km_fz_temp.where(km_fz_temp['is_fz_y']<1).dropna(axis=0,how='all')
balance_item_temp['qcye'] = balance_item_temp['qcye'].fillna(value=0)
balance_item_temp['jffse'].fillna(value=0,inplace=True)
balance_item_temp['dffse'].fillna(value=0,inplace=True)
balance_item_temp['qmye'].fillna(value=0,inplace=True)

# 左连接 插入期初余额到balance_item中，直插入最下层数据
    # 部分数据通过all_name 链接起来，部分数据通过fzmc链接起来
balance_item_temp2 = pd.merge(left=balance_item_temp,right=fz_item,how='left',left_on='kmmc',right_on='all_name')
balance_item_temp3 = pd.merge(left=balance_item_temp2,right=fz_item,how='left',left_on='kmmc',right_on='fzmc')
    # 合并辅助账，并进行重命名
def format_fz_combine(row):
    # 统一辅助项目编号
    if(str(row['fzbh_y']) != 'nan'):  # all_name部分拼接
        row['kmbh'] = row['fzbh_y']
        row['kmmc'] = row['fzmc_y']
        row['grade_x'] = row['grade_y']
    elif(str(row['fzmc_x']) != 'nan' and str(row['fzbh_y']) == 'nan'):
        row['kmbh'] = row['fzbh_x']
        row['kmmc'] = row['fzmc_x']
    # 增加科目编号
    if(str(row['grade_x']) != 'nan'):
        row['subjcode'] = np.nan
    else:
        row['subjcode'] = row['kmbh']
    return row
# 得到辅助项目的编号，由于辅助项目进行了重新组织,然后结合凭证表进行计算即可
balance_item_temp4 = balance_item_temp3.apply(format_fz_combine,axis=1)[['subjcode','kmbh','kmmc','kmfx','bz','qcye']].ffill()
    # 将pz_new凭证表中的fzbh换成对应的fz_item表中的辅助编号
    # 定义函数，，用来处理辅助编号情况
def format_pz_bh(row,fz):
    if(str(row['fzbh']) != 'nan'):
        result_fzbh = []
        # 从fz项目表里查找对应的辅助编号
        fzbh = str(row['fzbh']).split(' ')
        for fzbh_temp in fzbh:
            df = fz[fz['all_name'].isin([fzbh_temp])]
            result_fzbh.append(str(df['fzbh'].min()))
        row['fzbh'] = ','.join(result_fzbh)
    return row
#      Apply的另一种使用方法
fz_pz = pz_new.apply(format_pz_bh,axis=1,args=(fz_item,))

#   凭证表的辅助编号可能有多个，但就按一个进行计算





