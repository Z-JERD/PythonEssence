import datetime
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class MtLibDebug:

    """
    符号说明：https://geek-docs.com/matplotlib/matplotlib-tutorial/matplotlib-numpy.html
    """

    def draw_plot(self):
        """
        绘制图表

        只传递数组传递给plt.plot()函数，matplotlib会假定你所传入的是图表y值，
        于是将其跟一个序列的x值对应起来，x的取值依次为0，1，2，3

        图形表示的是一对(x, y)定义两个数组，其中第一个数组为x轴的各个值，第二个数组为y轴的值。
        此外plot()函数还可以接收第三个参数，它描述的是数据点在图表中的显示方式 默认 用蓝色线条连接各数据点

        """

        # 1. 只传递一个数组

        # plt.plot([1, 2, 3, 4])

        # 2. 传递 x值 y值并用红点显示各数据

        # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

        # 3. axis() 和 title

        # 定义x, y轴取值范围 把该列表作为参数传递给axis()函数
        # plt.axis([0, 5, 0, 20])

        # 设置标题 fontsize文本大小
        # plt.title("PlotExamples", fontsize=20)

        # 4. xlabel()和ylabel() 为x轴和y轴添加文本标签

        # plt.axis([0, 5, 0, 20])

        # plt.title("PlotExamples")

        # plt.xlabel("x_value")
        # plt.ylabel("y_value")

        # 5. text() 函数  在每个数据点旁边添加描述

        plt.figure(figsize=(10, 4), dpi=80)  # 图片长宽和清晰度
        plt.axis([0, 5, 0, 20])

        plt.title("PlotExamples")

        plt.xlabel("x_value")
        plt.ylabel("y_value")

        plt.text(1, 2.5, 'First')
        plt.text(2, 4.5, 'Second')
        plt.text(3, 9.5, 'Third')
        plt.text(4, 16.5, 'Fourth')

        # 添加表达式 表达式内容置于两个$符号之间

        plt.text(1.1, 12, r'$y=x^2$', fontsize=20, bbox={
            'facecolor': 'yellow', 'alpha': 0.2})

        # 6. 添加网格 grid() 函数

        # grid()函数 参数设置为True, 默认是实线

        # plt.grid(True)

        # 设置成虚线, 修改linestyle 参数  color:网格颜色
        plt.grid(True, linestyle="--", color='k')

        # 7. 设置图例 legend()

        plt.plot([1, 2, 3, 4], [1.8, 3.5, 8, 15], 'g^')
        plt.plot([1, 2, 3, 4], [1.5, 2.5, 4, 12], 'b*')

        plt.plot([1, 2, 3, 4], [2, 4, 9, 16], 'ro')   # b 折线图

        plt.legend(['First series', 'Second Series', 'Third series'], loc=2)

        plt.show()

        return

    def draw_plot_dk(self):
        """
        两条轴穿过原点(0,0)，就是笛卡儿坐标轴

        使用gca()函数获取Axes对象，通过这个对象指定每条边的位置：上、下、左、右。
        使用set_color()函数，把颜色设置为none，删除跟坐标轴不符合的边(右和上)，
        然后用set_position()函数移动跟x轴和y轴相符的边框，使其穿过原点（0，0）
        """
        x = np.arange(-2*np.pi, 2*np.pi, 0.01)
        y = np.sin(x*3)/x
        y2 = np.sin(x*2)/x
        y3 = np.sin(x*1)/x

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")
        plt.plot(x, y, color='b')
        plt.plot(x, y2, color='r')
        plt.plot(x, y3, color='g')

        # x轴, y轴的取值范围：

        plt.xticks(
                [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
                [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$']
            )

        plt.yticks(
            [-1, 0, +1, +2, +3],
            [r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$']
        )

        """
        用注释和箭头标明曲线上某个数据点的位置，这一功能非常有用。matplotlib库的annotate()函数特别适用于添加注释。
        它的参数设置略显繁琐，第一个参数为含有LaTex表达式，要在图形中显示的字符串。xy属性表示注释在图表中的位置。
        xytext属性表示文本注释跟它解释的数据点之间的距离。arrowprops属性表示箭头的属性。
        """

        plt.annotate(
                r'$\lim_{x\to 0}\frac{sin(x)}{x}=1$',
                xy=[0, 1],
                xycoords='data',
                xytext=[40, 40],
                fontsize=20,
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle="arc3, rad=.2")
            )

        ax = plt.gca()

        # 去掉上方和右边边框
        ax.spines['right'].set_color('None')
        ax.spines['top'].set_color('None')

        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))

        plt.show()

        return

    def frame2plot(self):
        """将DataFrame转换成图表"""

        data = {
            'series1': [1, 3, 4, 3, 5],
            'series2': [2, 4, 5, 2, 4],
            'series3': [3, 2, 3, 1, 3]
        }

        df = pd.DataFrame(data)

        x = np.arange(5)
        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")
        plt.axis([0, 5, 0, 7])
        plt.plot(x, df)

        plt.legend(data, loc=2)
        plt.show()

        return

    def draw_hist(self):
        """绘制直方图
        hist 参数：

            data: 必选参数，绘图数据
            bins: 直方图的长条形数目，可选项，默认为10
            facecolor: 长条形的颜色
            edgecolor: 长条形边框的颜色
            alpha:透明度

        x轴区间范围为info的取值范围
        y轴区间范围为各个元素数量的统计

        """

        # info = [
        #     1, 1, 5, 5, 2, 4, 4, 4, 8, 6
        # ]

        # plt.hist(info, bins=10)
        # plt.show()

        # 设置matplotlib正常显示中文和负号
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 用黑体显示中文
        matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号

        # 随机生成（10000,）服从正态分布的数据
        data = np.random.randn(100)
        plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)

        # 显示横轴标签
        plt.xlabel("区间")

        # 显示纵轴标签
        plt.ylabel("频数/频率")

        # 显示图标题
        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")

        plt.show()

        return

    def draw_bar(self):
        """
        绘制条形图
        """

        # index, values = [0, 1, 2, 3, 4], [10, 20, 30, 40, 50]

        # plt.title("geek_docs.com", fontsize=20, fontname="Times New Roman")

        # plt.bar(index, values)

        # plt.xticks(index, ['A', 'B', 'C', 'D', 'E'])

        # plt.show()

        # 添加图例
        """
        把标准差的列表传给yerr参数，就能添加标准差。

        error_kw：用于接收其他可用于显示误差线的关键字参数。eColor参数指定误差线的颜色，capsize参数指定误差线两头横线大的宽度。
        alpha：控制彩色条形图的透明度，取值范围是0-1，0表示完全透明，随alpha的增加，对象逐渐清晰起来，到1时不透明。
        label：为图表中的序列指定名称。
        """

        index, values = [0, 1, 2, 3, 4], [10, 20, 30, 40, 50]

        std1 = [0.8, 1, 0.4, 0.9, 1.3]

        plt.title("geek_docs.com", fontsize=20, fontname="Times New Roman")

        plt.bar(index, values, yerr=std1, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')

        plt.xticks(index, ['A', 'B', 'C', 'D', 'E'])
        plt.legend(loc=2)
        plt.show()

        return

    def draw_barh(self):
        """
        水平条形图

        类别分布在y轴上，数值显示在x轴上

        """

        index = np.arange(5)
        values1 = [5, 7, 3, 4, 6]
        std1 = [0.8, 1, 0.4, 0.9, 1.3]

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")
        plt.barh(index, values1, xerr=std1, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')

        plt.yticks(index, ['A', 'B', 'C', 'D', 'E'])
        plt.legend(['First series'], loc=5)
        plt.show()

        return

    def draw_date(self):
        """处理日期"""

        # 获取每月数据
        months = mdates.MonthLocator()

        # 获取每日数据
        days = mdates.DayLocator()

        events = [
            datetime.date(2015, 1, 23), datetime.date(2015, 1, 28),
            datetime.date(2015, 2, 3), datetime.date(2015, 2, 21),
            datetime.date(2015, 3, 15), datetime.date(2015, 3, 24),
            datetime.date(2015, 4, 8), datetime.date(2015, 4, 24)
        ]

        readings = [12, 22, 25, 20, 18, 15, 17, 14]

        fig, ax = plt.subplots()

        plt.plot(events, readings)

        # 设定主/次刻度
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_minor_locator(days)

        # 设定格式
        timeFmt = mdates.DateFormatter('%Y-%m')
        ax.xaxis.set_major_formatter(timeFmt)

        # 如果日期过长, 可设置旋转 rotation：旋转的大小
        plt.setp(ax.get_xticklabels(), rotation=5, horizontalalignment='right')

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")

        plt.show()

        return

    def draw_pie(self):
        """
        绘制饼图

        labeldistance: 文本的位置离远点有多远，1.1指1.1倍半径的位置

        autopct: 圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数

        shadow: 饼是否有阴影

        startangle: 起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看

        pctdistance: 百分比的text离圆心的距离

        plt.pie的返回值：
            patches, l_texts, p_texts, 为了得到饼图的返回值,
            p_texts饼图内部文本的, l_texts饼图外label的文本
        """

        labels = ['frogs', 'hogs', 'dogs', 'logs']

        # 每个标签占多大，会自动去算百分比
        sizes = [15, 20, 35, 25]

        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

        # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他的间隙
        explode = (0, 0.1, 0, 0)

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")

        plt.pie(
            sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=False, startangle=90
            )

        plt.axis('equal')

        plt.show()

        return

    def three_d_surface(self):
        """
        3D绘图： 曲面图, 散点图, 条形图
        """
        # 1. 曲面图 plot_surface()

        def f(x, y):

            return (1 - y**5 + x**5)*np.exp(-x**2-y**2)

        fig = plt.figure()
        ax = Axes3D(fig)

        X = np.arange(-2, 2, 0.1)
        Y = np.arange(-2, 2, 0.1)
        X, Y = np.meshgrid(X, Y)

        # cmap指定颜色
        ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1, cmap=plt.cm.hot)
        # view_init()函数旋转曲面 elev指定从哪个高度查看曲面，azim参数指定曲面旋转的角度
        ax.view_init(elev=30, azim=125)

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")

        plt.show()

        return

    def three_d_scatter(self):
        """
        3D散点图
        """

        xs = np.random.randint(30, 40, 100)
        ys = np.random.randint(20, 30, 100)
        zs = np.random.randint(10, 20, 100)

        xs2 = np.random.randint(50, 60, 100)
        ys2 = np.random.randint(30, 40, 100)
        zs2 = np.random.randint(50, 70, 100)

        xs3 = np.random.randint(10, 30, 100)
        ys3 = np.random.randint(40, 50, 100)
        zs3 = np.random.randint(40, 50, 100)

        fig = plt.figure()
        ax = Axes3D(fig)

        ax.scatter(xs, ys, zs)
        ax.scatter(xs2, ys2, zs2, c='r', marker='^')
        ax.scatter(xs3, ys3, zs3, c='g', marker='*')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z label')

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")
        plt.show()

        return

    def three_d_bar(self):
        """
        条形图
        """
        x = np.arange(8)
        y = np.random.randint(0, 10, 8)
        y2 = y + np.random.randint(0, 3, 8)
        y3 = y2 + np.random.randint(0, 3, 8)
        y4 = y3 + np.random.randint(0, 3, 8)
        y5 = y4 + np.random.randint(0, 3, 8)
        clr = ['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4']

        fig = plt.figure()
        ax = Axes3D(fig)

        ax.bar(x, y, 0, zdir='y', color=clr)
        ax.bar(x, y2, 10, zdir='y', color=clr)
        ax.bar(x, y3, 20, zdir='y', color=clr)
        ax.bar(x, y4, 30, zdir='y', color=clr)
        ax.bar(x, y5, 40, zdir='y', color=clr)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z label')

        ax.view_init(elev=40)

        plt.title("geek-docs.com", fontsize=20, fontname="Times New Roman")
        plt.show()

        return


if __name__ == "__main__":

    application = MtLibDebug()
    application.three_d_scatter()
