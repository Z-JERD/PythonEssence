import datetime

import pandas as pd
import numpy as np


class PracTiceSerice:

    def __init__(self):

        self.nt_date = datetime.datetime.now()

        # index中长度与data中长度不一致，将引发ValueError

        self.se_index = ["序号", "名称", "金额", "日期", "时间"]

    def list_serice_v1(self):
        """数组创建Series 未指定索引"""

        pd_data = [1, "测试", 100.25, f"{self.nt_date:%Y-%m-%d}", self.nt_date]
        df = pd.Series(pd_data)

        print(df)

        print(df.values, type(df.values))

        return

    def list_serice_v2(self):
        """指定索引"""

        pd_data = [1, "测试", 100.25, f"{self.nt_date:%Y-%m-%d}", self.nt_date]
        df = pd.Series(pd_data, index=self.se_index)

        print(df)

        print(df.values, type(df.values))

        return

    def dict_serice_v1(self):
        """字典创建Series 未指定索引"""

        pd_data = {
            "a": 1,
            "b": "测试",
            "c": 100.25,
            "d": f"{self.nt_date:%Y-%m-%d}",
            "e":  self.nt_date
        }

        df = pd.Series(pd_data)

        print(df)

        print(df.values, type(df.values))

        # 通过位置取值

        print(df[1])

        print(df[-2:])

        # 通过索引取值

        print(df["c"])

        print(df[["c", "d", "e"]])

        return

    def dict_serice_v2(self):
        """指定索引"""

        pd_data = {
            "a": 1,
            "b": "测试",
            "c": 100.25,
            "d": f"{self.nt_date:%Y-%m-%d}",
            "e":  self.nt_date
        }

        df = pd.Series(pd_data, index=self.se_index)

        df = df.fillna("")

        print(df)

        print(df.values, type(df.values))

        return

    def scalar_serice(self):

        # 不加索引, 就一个值, 加上索引, 重复该值

        df1 = pd.Series(5)

        df2 = pd.Series(5, index=[0, 1, 2, 3])

        print(df1, df2)

        print(df1.values, type(df1.values))

        return

    # =============================================================

    def list_frame_v1(self):
        """列表创建数据帧"""

        # 1. 传递单个列表, 列表中的每个数据都作为一行数据

        data1 = [1, "测试", 100.25, f"{self.nt_date:%Y-%m-%d}", self.nt_date]

        df = pd.DataFrame(data1)

        print(df)

        print(df.values, type(df.values))

        return

    def list_frame_v2(self):
        """二维列表创建"""

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

        return

    def list_frame_v3(self):
        """列表中套字典"""
        # 字典中的key作为行的索引, 以最长的字典为准, 不存在key的数据值为NaN

        data = [
            {'影院编码': 15010971, '影院名称': 'CGV星聚汇影城呼和浩特中山店'},
            {'影院编码': 12040771, '影院名称': 'CGV影城天津黄河道店', '开业时间': "2021-03-25"}]

        df = pd.DataFrame(data)

        # 指定行索引, 若行索引的值不在字典中的key中, 值为None

        df1 = pd.DataFrame(data, index=['first', 'second'], columns=['影院名称', '停业时间'])

        print(df)

        print(df1)

        print(df.values, type(df.values))

        return

    def dict_frame_v1(self):
        """字典中套数组"""

        # 字典中的key作为行索引, 每个value作为一列数据, value中长度必须一致  未指定列索引, 索引为range(n)

        data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-03025"]
        }

        df = pd.DataFrame(data)

        print(df)

        print(df.values, type(df.values))

        return

    def serices2_frame_v1(self):
        """一维数组创建数据帧"""

        data = {
            "影院编码": pd.Series([15010971, 12040771], index=['a', 'b']),
            "影院名称": pd.Series(
                ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '安徽金安红叶影城'],
                index=['a', 'b', 'c'])
        }

        df = pd.DataFrame(data)

        print(df)

        print(df.values, type(df.values))

        return

    def serices2_frame_v2(self):
        """一维数组创建数据帧"""

        data = {
            "影院编码": pd.Series([15010971, 12040771]),
            "影院名称": pd.Series(
                ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '安徽金安红叶影城'])
        }

        df = pd.DataFrame(data)

        print(df)

        print(df.values, type(df.values))

        return

    def get_frame_value(self):
        """DataFrame取值"""

        data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-03-25"]
        }

        df = pd.DataFrame(data)

        # 取单列值， 返回值为单数组

        # df_v1 = df["影院名称"]

        # 获取多列值， 返回值为数组套数组

        # df_v1 = df[["影院名称", "开业时间"]]

        # 根据位置获取单行值  返回值为单数组

        # df_v1 = df.iloc[0]

        # 获取多行值  返回值为数组套数组

        # df_v1 = df.iloc[1:3]

        df_v1 = df.loc[:]
        print(df_v1)
        print(df_v1.values, type(df_v1.values))

        return

    def frame_column(self):
        """列操作"""

        data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-030-25"]
        }

        df = pd.DataFrame(data)

        # 1. 添加列

        df["所属院线"] = pd.Series(['华夏联合', '上海联合', '中影星美'])

        # 列之间相互组合, 值得类型需要保持一致

        df["其他"] = df["影院名称"] + "（" + df["开业时间"] + "）"

        # 2. 删除列 

        del df["其他"]

        # df.pop("所属院线")

        print(df)

        print("\n================\n")

        print(df.values, type(df.values))

        return

    def frame_row(self):
        """行操作"""

        data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-03-25"]
        }

        df = pd.DataFrame(data, index=["A", "B"])

        # 1. 添加单行

        new_row = pd.DataFrame([
            [11067401, '华夏国际影城', '2021-03-26']
        ],  columns=['影院编码', '影院名称', '开业时间'], index=["C"])

        # 添加多行
        new_row = pd.DataFrame([
            [42015101, '武汉环艺新民众乐园', '2021-03-21'],
            [42011001, '江汉环球影城', '2021-03-27']
        ],  columns=['影院编码', '影院名称', '开业时间'], index=["D", "E"])

        df = df.append(new_row)

        # 2. 删除行  根据索引标签删除

        df = df.drop("E")

        print(df)

        print("\n================\n")

        print(df.values, type(df.values))

        return

    def frame_index(self):
        """修改索引项"""

        data = {
            "影院编码": [15010971, 12040771],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店'],
            "开业时间": ["2021-03-24", "2021-03-25"]
        }

        df = pd.DataFrame(data)

        print(df)

        print("\n-------------\n")

        # 1. 修改表头索引

        # df.columns = ["影院编码v1", "影院名称v1", "开业时间v1"]

        # 2. 修改列索引

        # df.index = ["A", "B"]

        # 3. rename 映射替换

        df = df.rename(
            columns={"影院编码": "影院编码V1", "影院名称": "影院名称V1", "开业时间": "开业时间V1"},
            index={0: "A", 1: "B"}
            )

        print(df)

        return

    def frame_iter(self):
        """pandans迭代操作"""
        # iteritems()： 将每个列索引作为键, 每列的数据作为value

        df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])

        print(df)

        print("\n------------------\n")

        # for key, value in df.iteritems():

        #     print(value)

        # iterrowss()： 将每个行索引作为键, 每行的数据作为value

        for row_index, row in df.iterrows():

            print(row)

        # itertuples() 每一行返回一个产生一个命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。

        # for row in df.itertuples():  
        #     print(row)

        return

    def frame_sort(self):
        """对DataFrame排序处理"""

        df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])

        print(df)

        # 1. sort_index() 根据索引排序 默认对行索引升序, ascending=False 降序

        sorted_df = df.sort_index()

        sorted_dec_df = df.sort_index(ascending=False)

        print(sorted_df)

        print(sorted_dec_df)

        # 2. 按列排序 过传递axis参数值为0或1，可以对列标签进行排序。 默认情况下，axis = 0，逐行排列

        sort_col_df = df.sort_index(axis=1)

        print(sort_col_df)

        # 3. sort_values() 按值进行排序 by参数指定列索引

        sorted_value_df = df.sort_values(by='col1')

        # 指定多列进行排序
        sorted_multi_df = df.sort_values(by=['col1', 'col2'],  ascending=False)

        print(sorted_value_df)
        print(sorted_multi_df)

        return

    def frame_index_colums(self):
        """索引和选择数据"""

        # loc()主要基于标签(label)， 即行名称和列名称
        # df.loc[index_name, col_name]选择指定位置的数据

        df = pd.DataFrame(
            np.random.randn(8, 4),
            index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            columns=['A', 'B', 'C', 'D']
            )

        print(df)
        print("\n====================\n")

        # 1. 获取'A'行所有数据
        print(df.loc[:, 'A'])

        # 2. 获取多行数据

        print(df.loc[:, ['B', 'C']])

        # 3. 指定特定行，特定列

        print(df.loc[['a', 'b'], ['B', 'C']])

        # 4. 获取特定行,特定列的值

        print(df.loc['b', 'D'])

        # .iloc() 基于整数的索引，利用元素在各个轴上的索引序号进行选择 小标从 0 开始。 
        
        # 1. 索引取行值  df.iloc[0:3]， 只包含 0，1，2行

        print(df.iloc[: 4])

        # 2. 指定列值

        print(df.iloc[:4, 2:4])

        # 3. 指定行值 df.iloc[[5, 1, 7]]，选择第 6 行， 第 2 行， 第 8 行      
        
        print(df.iloc[[1, 3, 5], [1, 3]])

        return

    def frame_nan_deal(self):
        """NaN缺失值处理"""
        # 1. Series去掉NaN

        df = pd.Series([0, 1, 2, np.NaN, 9], index=['red', 'blue', 'yellow',
                                                    'white', 'green'])

        print(df)

        df = df.dropna()

        print(df)

        # 2. DataFrame去掉NaN

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

        # NaN元素填充其他值： .fillna

        # 1. 所有NaN补充一样的值

        print(df.fillna(0))

        # 2. 不同列的NaN替换为不同的元素

        print(df.fillna({"ball": 1, "mug": 2, "pen": 3}))

        return

    def frame_groupby(self):
        """分组应用"""
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

        # 1. 统计各颜色的 pencil  
        #.groups查看每个分组所在行  .mean()查看分组均值  .sum()查看分组总值

        group = df['price1'].groupby(df['color'])
        print(group.groups)
        print(group.mean())
        print(group.sum())

        # 2. 等级分组

        # 指定统计列

        print(df[['price1', 'price2']].groupby(df['color']).sum())

        # 统计所有的数值列
        print(df.groupby(df['color']).sum())

        # 指定多个分组

        res = df['price1'].groupby([df['color'], df['object']]).sum()

        print(res)

        return

    def frame_merge(self):
        """合并"""

        frame1 = pd.DataFrame(
            {
                'id': ['ball', 'pencil', 'pen', 'mug', 'ashtray'],
                'color': ['white', 'red', 'red', 'black','green'],
                'brand': ['OMG', 'ABC', 'ABC', 'POD', 'POD']
            }
        )
       
        frame2 = pd.DataFrame(
            {
                'id': ['pencil', 'pencil', 'ball', 'pen'],            
                'brand': ['OMG', 'POD', 'ABC', 'POD']
            }
        )

        print(frame1)

        print("\n===============\n")

        print(frame2)

        print("\n===============\n")

        print(pd.merge(frame1, frame2, on='id'))
        
        print("\n------------\n")
        
        print(pd.merge(frame1, frame2, on='brand'))

        return
    
    def frame_concat(self):
        """DataFrame拼接 concat()"""
        # concat()函数实现了按索引拼接的

        # 1. Series拼接

        ser_data1 = ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '武汉环艺新民众乐园']
        ser_data2 = ['南京工人影城', '常州亚细亚影视城', '南京上影华纳影城']

        ser1 = pd.Series(ser_data1, index=[0, 1, 2])

        ser2 = pd.Series(ser_data2, index=[3, 4, 5])

        sd = pd.concat([ser1, ser2])

        print(sd)

        # 指定axis=1，返回结果将是DataFrame对象

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

        # 等级索引  用于拼接的轴上创建等级索引，可以借助keys选项来完成

        sd_1 = pd.concat([ser1, ser2], keys=[1, 2])

        print(sd_1)

        # 按照axis拼接Series对象，指定的键变成拼接后得到的DataFrame对象列的名称

        sd_2 = pd.concat([ser1, ser2], keys=[1, 2], axis=1)

        print(sd_2)

        # DataFrame拼接操作

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

        return

    def frame_del(self):
        """删除数据 drop"""

        ser_data1 = ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '武汉环艺新民众乐园']
        se_1 = pd.Series(ser_data1)

        print(se_1)
        print("\n----------------\n")

        # 1. 删除某行数据
        se_2 = se_1.drop(1)

        print(se_2)

        print("\n----------------\n")

        # 2. 删除多行数据

        se_3 = se_1.drop([0, 1])

        print(se_3)
        print("\n----------------\n")
        
        dt_1 = {
            "影院编码": [15010971, 12040771, 32011801, 32060302],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV影城天津黄河道店', '南京万达国际影城（新街口店）', '扬州工人文化宫'],
            "开业时间": ["2021-03-24", "2021-03-25", "2021-03-26", "2021-03-27"]
        }

        fm_1 = pd.DataFrame(dt_1)

        print("\n----------------\n")

        # 1. 删除某行数据

        res_1 = fm_1.drop(2)

        print(res_1)

        print("\n----------------\n")

        # 2. 删除多行数据

        res_2 = fm_1.drop([1, 2])

        print(res_2)

        print("\n----------------\n")

        # 3. 删除指定的列

        res_4 = fm_1.drop("影院编码", axis=1)

        print(res_4)

        print(fm_1)

        print("\n----------------\n")

        #  4. 删除多列

        res_5 = fm_1.drop(["影院编码", "开业时间"], axis=1)

        print(res_5)

        # 删除重复行

        dt_2 = {
            "影院编码": [15010971, 15010971, 32011801, 32060302],
            "影院名称": ['CGV星聚汇影城呼和浩特中山店', 'CGV星聚汇影城呼和浩特中山店', '南京万达国际影城（新街口店）', '扬州工人文化宫'],
            "开业时间": ["2021-03-24", "2021-03-24", "2021-03-26", "2021-03-27"]
        }

        fm_2 = pd.DataFrame(dt_2)

        print(fm_2)

        res2_1 = fm_2.drop_duplicates()

        print(res2_1)

        print(fm_2)
              
        return


if __name__ == "__main__":

    application = PracTiceSerice()
    application.frame_del()
