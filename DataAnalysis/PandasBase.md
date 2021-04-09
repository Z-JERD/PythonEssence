# Series

    Series是由相同数据类型组成的一维数组

## Series 关键信息:

    同种类型数据构成
    大小不可变
    数据可变

## pandas.Series( data, index, dtype, copy)

### 参数说明：

    参数	说明
	
    data	支持多种数据类型，如：ndarray，list，constants
	
    index	索引值必须是唯一的，与data的长度相同，值为数组， 没有传递索引值，
            那么默认的索引范围将range(n)
	
    dtype	数据类型
	
    copy	是否复制数据，默认为false

## 数组创建Series

    nt_date = datetime.datetime.now()

    # index中长度与data中长度不一致，将引发ValueError

    pd_index = ["序号", "名称", "金额", "日期", "时间"]

    pd_data = [1, "测试", 100.25, f"{nt_date:%Y-%m-%d}", nt_date]

    df = pd.Series(pd_data, index=pd_index)

    print(df)

    print(df.values)    

## 字典创建Series

    没有指定索引，则按排序从字典中取得键值作为索引, 传递了索引，则去字典中寻找对应的key, key不存在，值为NaN

    pd_data = {
        "a": 1,
        "b": "测试",
        "c": 100.25,
        "d": f"{nt_date:%Y-%m-%d}",
        "e":  nt_date
    }

    df1 = pd.Series(pd_data)

    df2 = pd.Series(pd_data, index=pd_index)

    print(df)

    print(df.values, type(df.values))

    序号    NaN
    名称    NaN
    金额    NaN
    日期    NaN
    时间    NaN
    dtype: object
   
    [nan nan nan nan nan] <class 'numpy.ndarray'>

## 标量创建Series

    # 不加索引, 就一个值, 加上索引, 重复该值

    df1 = pd.Series(5)

    df2 = pd.Series(5, index=[0, 1, 2, 3])

    print(df1, df2)

## Series取值

    1. 通过位置取值： df[0], df[2: 4]

    2. 通过索引取值： df['序号'], df[['序号', '名称', '金额']]

# DataFrame(数据帧)

    每列可以是不同的数据类型

## DataFrame 关键信息：

    可以由不同的数据类型构成
    大小可变
    数据可变

## pandas.DataFrame( data, index, columns, dtype, copy)

### 参数说明：

    参数	说明
    
    data	支持多种数据类型，如:ndarray，series，map，lists，dict，constant和另一个DataFrame。
    
    index	行标签，如果没有传递索引值，默认值为np.arrange(n)
    
    columns	列标签，如果没有传递索引值，默认值为np.arrange(n)
    
    dtype	每列的数据类型。
    
    copy	是否复制数据，默认值为False

## 列表创建DateFrame
    
    列表中的每个数据都作为一行数据

### 1. 单个列表创建数据帧

    data1 = [1, "测试", 100.25, f"{self.nt_date:%Y-%m-%d}", self.nt_date]

    df = pd.DataFrame(data1)

    print(df)

    print(df.values, type(df.values))

### 2. 二维列表创建

        data = [
                    [15010971, 'CGV星聚汇影城呼和浩特中山店'],
                    [12040771, 'CGV影城天津黄河道店'],
                    [31142101, 'SFC上影影城（南桥百联店）'],
                    [34131301, '安徽金安红叶影城'],
                    [41053201, '安阳市奥斯卡激光巨幕影城']
                ]

        columns = ["影院编码", "影院名称"]

        df = pd.DataFrame(data)

        df1 = pd.DataFrame(data, columns=columns)

        print(df, df1)

        print(df.values, type(df.values))

### 3. 列表中套字典

    字典中的key的集合作为行的索引, 不存在key的字典对应的数据值为NaN

     data = [
                {'影院编码': 15010971, '影院名称': 'CGV星聚汇影城呼和浩特中山店'},
                {'影院编码': 12040771, '影院名称': 'CGV影城天津黄河道店', '开业时间': "2021-03-25"}
            ]

    df = pd.DataFrame(data)

    # 指定行索引, 若行索引的值不在字典中的key中, 值为NaN

    df1 = pd.DataFrame(data, index=['first', 'second'], columns=['影院名称', '停业时间'])

## 字典创建DateFrame

    字典中的key作为行索引, 每个value作为一列数据, value中长度必须一致

    未指定列索引, 索引为range(n)

    data = {
        "影院编码": [15010971, 12040771],
        "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
        "开业时间": ["2021-03-24", "2021-03025"]
    }

    df = pd.DataFrame(data)

    print(df)

    print(df.values, type(df.values))

## 一维数组创建数据帧

    一维数组的长度不必保持一致

### 未指定列索引

        data = {
            "影院编码": pd.Series([15010971, 12040771]),
            "影院名称": pd.Series(
                ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '安徽金安红叶影城'])
        }

        df = pd.DataFrame(data)

        print(df)

        print(df.values, type(df.values))


### 指定列索引

        data = {
                    "影院编码": pd.Series([15010971, 12040771], index=['a', 'b']),
                    "影院名称": pd.Series(
                        ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '安徽金安红叶影城'],
                        index=['a', 'b', 'c'])
                }

        df = pd.DataFrame(data)

        print(df)

        print(df.values, type(df.values))

## DataFrame取值

    data = {
                "影院编码": [15010971, 12040771],
                "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
                "开业时间": ["2021-03-24", "2021-03025"]
            }

    df = pd.DataFrame(data)

### 取列值

    取单列值, 返回值为单数组： 
        
        df_v1 = df["影院名称"]

    获取多列值, 返回值为数组套数组：

        df_v1 = df[["影院名称", "开业时间"]]

### 取行值

    根据位置取值：iloc

        取单行值, 返回值为单数组:

            df_v1 = df.iloc[0]

        取多行值  返回值为数组套数组:

            df_v1 = df.iloc[1:3]

    根据索引取值：

         取单行值, 返回值为单数组:

            df_v1 = df.loc[0]

        取多行值  返回值为数组套数组:

            df_v1 = df.loc[:]

## DataFrame添值，删值

    data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-03-25"]
        }

    df = pd.DataFrame(data, index=["A", "B"])

### 列操作

#### 1. 添加列

    df["所属院线"] = ['华夏联合', '上海联合']

    df["所属院线"] = pd.Series(['华夏联合', '上海联合'])

    # 列之间相互组合, 值得类型需要保持一致

    df["其他"] = df["影院名称"] + "（" + df["开业时间"] + "）"

#### 2. 删除列 根据索引标签删除

    drop: 返回值为修改后的数据， 原数据不会被修改。删除列需指定axis=1
    pop: 返回值为删除的数据，原数据修改

    del df["其他"]       df数据变更

    df.pop("所属院线")   返回值为删除的数据, df数据变更

    df = df.drop("影院编码", axis=1)

    # 删除多列

    df = df.drop(["影院编码", "开业时间"], axis=1)


### 行操作

#### 1. 添加行
    
     添加单行：

        new_row = pd.DataFrame([
            [11067401, '华夏国际影城', '2021-03-26']
        ],  columns=['影院编码', '影院名称', '开业时间'], index=["C"])
    
    添加多行：

        new_row = pd.DataFrame([
            [42015101, '武汉环艺新民众乐园', '2021-03-21'],
            [42011001, '江汉环球影城', '2021-03-27']
        ],  columns=['影院编码', '影院名称', '开业时间'], index=["D", "E"])

    df = df.append(new_row)

#### 2. 删除行

    根据索引标签删除，如果标签重复，则会删除多行

        df = df.drop(0)             由于数据的索引为 A, B, C, D, E  此处代码报错

        df = df.drop("E")           返回值为变更后的数据, 原数据未变 
 
        df = df.drop(["D", "E"])    删除多行数据

        df = df.drop_duplicates()   删除重复行, 返回值为变更后的数据, 原数据未变 


## DataFrame修改索引项


    data = {
        "影院编码": [15010971, 12040771],
        "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
        "开业时间": ["2021-03-24", "2021-03-25"]
    }

    df = pd.DataFrame(data)


### 1. 修改表头索引

    df.columns = ["影院编码v1", "影院名称v1", "开业时间v1"]     

### 2. 修改列索引
    
    df.index = ["A", "B"]

### 3. rename 映射替换

    df = df.rename(
                columns={"影院编码": "影院编码V1", "影院名称": "影院名称V1", "开业时间": "开业时间V1"},
                index={0: "A", 1: "B"} 
                )


## DataFrame的属性和方法

    1. df.T                           转置行和列
    
    2. df.empty                       判断对象是否为空

    3. df.shape                       返回元组(a，b)，其中a表示行数，b表示列数

    4. df.size                        返回 DataFrame 中的元素个数

    5. df.values                      将DataFrame中的实际数据作为NDarray返回

    6. df.head(n)                     返回前n行 默认数量为5

    7. df.tail()                      返回最后n行 默认数量为5
 
    8. df.index                       显示DataFrame的行索引

    9. df.columns                     显示DataFrame的列索引
    
    10. df.info()                     查看数据的信息 列出每列的信息
                                      字段过多，超过pandas的默认显示数量时，显示就给有缺失

                                      pd.get_option("max_info_columns")  默认显示数量信息

                                      pd.options.display.max_info_columns = 200  # 设置info中信息显示数量为200
## DataFrame 日期转换

    to_datetime

    data = {
        "影院编码": [15010971, 12040771],
        "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
        "开业时间": [20210324, 20210325]
    }

    df = pd.DataFrame(data)

    # 转换时间

    df["open_date"] = pd.to_datetime(df["开业时间"], format="%Y%m%d")

    # 提取月初日期

    df["open_date_f"] = df["open_date"].astype("datetime64[M]")

    # 提取年份   月：dt.month  日：dt.day
    df["open_year"] = df["open_date"].dt.year

    print(df)

## DataFrame的迭代

    df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])

    print(df)

    print("\n------------------\n")

        col1      col2      col3
    0  0.254561  0.511318 -0.713712
    1  1.594807 -0.351120  1.454376
    2 -1.309456  0.248841  0.719391
    3  3.120659  1.017098 -0.645118

### 1. iteritems()： 将每个列索引作为键, 每列的数据作为value
    
    for key, value in df.iteritems():
                print(value)

    0    0.254561
    1    1.594807
    2   -1.309456
    3    3.120659

### 2. iterrowss()： 将每个行索引作为键, 每行的数据作为value

    col1   -1.547325
    col2   -1.401118
    col3    0.671288

### 3. itertuples() 每一行返回一个产生一个命名元组的迭代器。
    
    元组的第一个元素将是行的相应索引值，而剩余的值是行值。

    for row in df.itertuples():
            
        print(row)


    Pandas(Index=0, col1=-0.9669162476447314, col2=-0.5268674192826223, col3=1.3449240625643342)
    Pandas(Index=1, col1=-0.18157706060714057, col2=1.3543709977727203, col3=-0.4885705500388794)
    Pandas(Index=2, col1=0.45031312102419424, col2=0.4383225350860488, col3=-0.46003589931768907)
    Pandas(Index=3, col1=-1.142771090802465, col2=-0.27637665445048254, col3=1.7894119393295973)

## DataFrame的排序

    df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])

    print(df)

### 1. sort_index() 根据索引排序
    
    默认对行索引升序, ascending=False 降序

        sorted_df = df.sort_index()

        sorted_dec_df = df.sort_index(ascending=False)

        print(sorted_df)

        print(sorted_dec_df)

    按列排序：
    
        传递axis参数值为0或1，可以对列标签进行排序。 默认情况下，axis = 0，逐行排列

        sort_col_df = df.sort_index(axis=1)

            print(sort_col_df)

### 2. sort_values() 按值进行排序 by参数指定列索引

    sorted_value_df = df.sort_values(by='col1')

    # 指定多列进行排序
    
    sorted_multi_df = df.sort_values(by=['col1', 'col2'],  ascending=False)

    print(sorted_value_df)
    
    print(sorted_multi_df)


## DataFrame的索引和选择数据

    df = pd.DataFrame(
            np.random.randn(8, 4),
            index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            columns=['A', 'B', 'C', 'D']
            )

    print(df)
    print("\n====================\n")

### 1. loc()主要基于标签(label)
    
    即行名称和列名称, df.loc[index_name, col_name]选择指定位置的数据

#### 1. 获取'A'行所有数据

    print(df.loc[:, 'A'])

#### 2. 获取多行数据
    
    print(df.loc[:, ['B', 'C']])

#### 3. 指定特定行，特定列

    print(df.loc[['a', 'b'], ['B', 'C']])

#### 4. 获取特定行,特定列的值

    print(df.loc['b', 'D'])

### 2. .iloc() 基于整数的索引

    利用元素在各个轴上的索引序号进行选择 小标从 0 开始

#### 1. 索引取行值  df.iloc[0:3]， 只包含 0，1，2行

        print(df.iloc[: 4])

#### 2. 指定列值

    print(df.iloc[:4, 2:4])

#### 3. 指定行值 df.iloc[[5, 1, 7]]，选择第 6 行， 第 2 行， 第 8 行      

    print(df.iloc[[1, 3, 5], [1, 3]])

## NaN缺失值处理

### 去掉NaN: dropna()

#### 1. Series去掉NaN
   
    df = pd.Series([0, 1, 2, np.NaN, 9], index=['red', 'blue', 'yellow',
                                                        'white', 'green'])

    print(df)

    df = df.dropna()

#### 2.  DataFrame去掉NaN

    df = pd.DataFrame(
             [[6, 7, 6], [np.nan, np.nan, np.nan], [2, np.nan, 5]],
             index=['blue', 'green', 'red'],
             columns=['ball', 'mug', 'pen']
            )

    print(df)
    
    # 1. 默认只要行或列有一个NaN元素，该行或列的全部元素都会被删除

    print(df.dropna())

    # 2. 指定 how='all' 数只删除所有元素均为NaN的行或列

    print(df.dropna(how="all"))

### NaN元素填充其他值： .fillna()
    
    # 1. 所有NaN补充一样的值

    print(df.fillna(0))

    # 2. 不同列的NaN替换为不同的元素

    print(df.fillna({"ball": 1, "mug": 2, "pen": 3}))


## 分组应用
    df = pd.DataFrame(
                {
                    'color': ['white', 'red', 'green', 'red', 'green'],
                    'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
                    'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
                    'price2': [4.75, 4.12, 1.60, 0.75, 3.15],
                    'num': [1, 2, 3, 4, 5]
                }
            )

    print(df)

### 1. 简单分组

    统计各颜色的 pencil
    .groups查看每个分组所在行  .mean()查看分组均值  .sum()查看分组总值

    group = df['price1'].groupby(df['color'])
    
    print(group.groups)
    print(group.mean())
    print(group.sum())

### 2. 等级分组

# 指定统计列

    print(df[['price1', 'price2']].groupby(df['color']).sum())

    # 统计所有的数值列
    print(df.groupby(df['color']).sum())

    # 指定多个分组

    res = df['price1'].groupby([df['color'], df['object']]).sum()

    print(res)

## DataFrame concat()

    concat()函数实现了按索引拼接的

### Series拼接

    ser_data1 = ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '武汉环艺新民众乐园']
    ser_data2 = ['南京工人影城', '常州亚细亚影视城', '南京上影华纳影城']

    ser1 = pd.Series(ser_data1, index=[0, 1, 2])

    ser2 = pd.Series(ser_data2, index=[3, 4, 5])

    sd = pd.concat([ser1, ser2])

    print(sd)

#### 1. 指定axis=1，返回结果将是DataFrame对象

    sd_x = pd.concat([ser1, ser2], axis=1)

    print(sd_x)

    """
                        0                     1
        
        0  CGV星聚汇影城呼和浩特中山店          NaN
        1      CGV影城天津黄河道店             NaN
        2        武汉环艺新民众乐园            NaN
        3              NaN                  南京工人影城
        4              NaN                  常州亚细亚影视城
        5              NaN                  南京上影华纳影城
        
    """

#### 2. 等级索引  
    
    用于拼接的轴上创建等级索引，可以借助keys选项来完成

        sd_1 = pd.concat([ser1, ser2], keys=[1, 2])

        print(sd_1)

    按照axis拼接Series对象，指定的键变成拼接后得到的DataFrame对象列的名称

        sd_2 = pd.concat([ser1, ser2], keys=[1, 2], axis=1)

        print(sd_2)

### DataFrame拼接操作

    dt_1 = {
                "影院编码": [15010971, 12040771],
                "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
                "开业时间": ["2021-03-24", "2021-03-25"]
            }

    dt_2 = {
        "影院编码": [32011801, 32060302],
        "影院名称": ['南京万达国际影城（新街口店）', '扬州工人文化宫'],
        "开业时间": ["2021-03-26", "2021-03-27"]
    }

    fm_1 = pd.DataFrame(dt_1)

    fm_2 = pd.DataFrame(dt_2)

    print(fm_1)

    print("\n-----------------\n")

    print(fm_2)

    print("\n------------------\n")

#### concat操作

    fm_3 = pd.concat([fm_1, fm_2])

    print(fm_3)

    print("\n-------------------\n")

    # 指定axis=1拼接数据

    fm_4 = pd.concat([fm_1, fm_2], axis=1)

    print(fm_4)

    """
        影院编码             影院名称        开业时间      影院编码            影院名称                开业时间
    
    0  15010971  CGV星聚汇影城呼和浩特中山店  2021-03-24  32011801  南京万达国际影城（新街口店）  2021-03-26
    1  12040771      CGV影城天津黄河道店  2021-03-25  32060302         扬州工人文化宫           2021-03-27
    
    """


# Panel(面板)

    由不同的数据类型构成的三维数据结构，Panel是DataFrame的容器

## Panel 关键信息

    可以由不同的数据类型构成
    大小可变
    数据可变




    
   
