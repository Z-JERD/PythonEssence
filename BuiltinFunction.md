# 常用的内置函数
    map filter zip 返回的是迭代器   sort对原列表进行排序  sorted 返回的是新的列表

# abs(x)
    返回一个数的绝对值。实参可以是整数或浮点数。如果实参是一个复数，返回它的模 
    abs(5 // 2)         2   
    abs(-5 // 2)        3
    //	取整除 返回商的整数部分（向下取整）

 # round(number,num_digits)
    对浮点数进行进行四舍五入
    Number 需要进行四舍五入的数字。
    Num_digits 指定的位数，按此位数进行四舍五入 不写的话默认保留到整数
    
    round(10.0/3, 2)    3.33
    round(20/7)         3
    
    不足之处：
        1. round的结果跟python版本有关
            round(0.5) python2中值为1 python3中值为0
        2. 特殊数字round出来的结果可能未必是想要的 
            round(2.675, 2)   值 2.67
            原因：
                机器中浮点数不一定能精确表达，因为换算成一串1和0后可能是无限位数的，机器已经做出了截断处理。
                那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点，
                所以保留两位小数时就近似到了2.67。
        
        对浮点数精度要求如果很高的话，用decimal模块
           
    
    
# divmod(a, b)
    把除数和被除数的运算结果结合起来，返回一个包含商和余数的元组
    
    1. 整数参数     
            divmod(9, 5)        值为(1, 4)
            divmod(23, 2)       值为(11, 1)
    2. 浮点数参数   
            divmod(2.3, 0.2)    值为(11.0, 0.0999999999999997)
            divmod(7.5, 1.5)    值为(5.0, 0.0)
            divmod(7, 3.5)      值为(2.0, 0.0)
            divmod(7.0, 2)      值为(3.0, 1.0)
          
          
          
 # lambda()
    匿名函数,减少了代码的冗余, 快速的实现某项功能
    形式：
        lambda argument_list:expersion
    argument_list是参数列表, 结构与Python中函数(function)的参数列表是一样的
    expression是一个关于参数的表达式
        常用：
        1. 直接赋给一个变量，然后再像一般函数那样调用
            c = lambda x, y, z: x*y*z
            c(2,3,4)
        2. 以在函数后面直接传递实参
            c = (lambda x:x**2)(3)
        3. 与map、filter、sorted、reduce等一些Python内置函数使用
            1. 生成列表[{'a':'c'},{'b':'d'}]
                tu1=(('a'),('b'))
                tu2=(('c'),('d')) 
            
                list(map(lambda x, y : {x : y},tu1,tu2))
            
            2. 生成列表[{'a':'c'},{'b':'d'}]
                tu1(('a',),('b',))
                tu2=(('c',),('d',)) 
                
                list(map(lambda x ,y : {x[0] : y[0]}, tu1, tu2))
        4. 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
            time.sleep=lambda x:None   # 屏蔽标准库time中的函数sleep的功能
            后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)时，程序不会休眠3秒钟，而是什么都不做
        
        5. 将lambda函数作为参数传递给其他函数
            函数的返回值也可以是函数。例如return lambda x, y: x+y返回一个加法函数
        
    更多：
        1. if/else
            ( lambda x, y: x if x < y else y )( 1, 2 )
        2. 科里化：
            ( lambda x: ( lambda y: ( lambda z: x + y + z  )( 1 ) )( 2 ) )( 3 )
        3. 递归：
            func = lambda n:1 if n == 0 else n * func(n-1)
            func(5)
            
            f = lambda func, n: 1 if n == 0 else n * func( func, n - 1 )
            f(f,4)
    
    
    
    
    
# max()/min()
    1.默认参数key为None
        li = [1, 5, 10, 20]
        print(max(li), min(li)
    
    2.自定义key
        dic={3:20,2:100,5:30}
        1.以Key值比较，取出最大值      max(dic.items(),key=lambda x: x )    #(5, 100)
        2.以Value值比较，取出最大值    max(dic.items(),key=lambda  x : x[1])
        
        
# zip()
    拉链方法。可将两个可迭代对象进行匹配
    可以放置多个可迭代对象,以最少的可迭代对象的个数为基准,返回一个迭代器
    1.可迭代对象长度一致
        li=["name","age"]
        li1=["jerd",18]
        print(dict(zip(li,li1)))
        
    2.可迭代对象长度不一致
    
        li=["name","age","hobby"]
        li1=["jerd",18]
        print(dict(zip(li,li1)))
        
    3.多个迭代对象进行匹配时
        li=["name","age","high"]
        li1=["jerd",18,"hobby"]
        li2=["xdd","book","play"]
        print(list(zip(li,li1,li2)))
        
        
        
# map(func, *iterables))
    可迭代对象的元素，一个一个传给函数
    1.list(map(lambda x : x**2 ,[1,2,3]))
    2.list(map(lambda x,y:x + y,[1,2,3,7],[4,5,6]))  [5, 7, 9]
    
    
    
    
# filter(function or None, iterable)
    过滤,取出符合条件的元素
    list(filter(lambda x : x % 2 == 0, [0,1,2,4]))
    
    
    
# sorted() 
    会形成新的列表，排序必须是列表
    li = ['fsdafsa','fddsaf','qqq','fgasjdlg;dsjfg']
    li2 = sorted(li,key=lambda x: len(x))
    li.sort(key=func)
    print(li, li2) 
    
    将dic中的内容以value值进行降序
        dic = {'math':90, 'chinese':99, 'english':66, 'history': 88, 'political':89,}
        new_dic = dict(sorted(dic.items(),key=lambda x : x[1], reverse=True))

    所有排序方法中，sorted的效率是最高的。它使用c代码编写的
        

# reduce()
    reduce()传入的函数 f 必须接收两个参数,reduce()对list的每个元素反复调用函数f，并返回最终结果值。
    Python3中,reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里
    from functools import reduce
    例:编写一个f函数，接收x和y，返回x和y的和：
        res = reduce(lambda x, y : x + y, [1, 3, 5, 7, 9])
        等同于：sum([1, 3, 5, 7, 9])
        
        计算过程：
            先计算头两个元素：f(1, 3)，结果为4；
            再把结果和第3个元素计算：f(4, 5)，结果为9；
            再把结果和第4个元素计算：f(9, 7)，结果为16；
            再把结果和第5个元素计算：f(16, 9)，结果为25；
            由于没有更多的元素了，计算结束，返回结果25。
            
            \
            
            
# hash(object)
    返回该对象的哈希值(int, str, bool, tuple, object)
    hash算法:
        (1) 目的是唯一性 
        (2) dict 查找效率非常高
        (3)hash表.用空间换的时间 比较耗费内存
        
    hash() 对对象使用时，所得的结果不仅和对象的内容有关，还和对象的 id()，也就是内存地址有关
    

# hex(x)
    将整数转换为以“0x”为前缀的小写十六进制字符串
    
    hex(255)
    hex(-42)
    
    如果要将整数转换为大写或小写的十六进制字符串，并可选择有无“0x”前缀
    format(255, '#x')         '0xff
    format(255, 'x')          'ff
    format(255, 'X')          'FF'
    

# float.hex()
    获取浮点数的十六进制字符串形式
        float.hex(3740.0)             '0x1.d380000000000p+11'
    float.fromhex(s)
        返回以十六进制字符串表示的浮点数
        float.fromhex( '0x1.d380000000000p+11')    3740.0
        

# repr()
    返回一个对象的string形式
    s = "明月几时有\n把酒问青天\t苏轼"
    print(s)
        明月几时有
        把酒问青天	苏轼

    print(repr(s))   
        '明月几时有\n把酒问青天\t苏轼'
        
# dir()
    查询一个类或者对象所有属性
    
    dir(函数名)与dir(函数名())有什么不同?
    
        def hello_python():
            name = "python
            return 'hello python'
        
        1. 使用 dir(hello_python), 得到这个函数(对象)的所有属性，
        2. 使用dir(hello_python()), 先执行hello()，再执行dir(返回值)，这里就是dir('hello python'),得到‘hello python’这个字符串对象的所有属性


    
 # help()
    了解模块、类型、对象、方法、属性的详细信息
    
    查看python所有的关键字：help("keywords")

    查看python所有的modules：help("modules")
    
    单看python所有的modules中包含指定字符串的modules： help("modules yourstr")

    查看python中常见的topics： help("topics")

# iter()和 next()
    iter() 将可迭代对象转换成迭代器
    next() 对迭代器取值
   
# enumerate(iterable, start=0)
    返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。 
    enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
    
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list(enumerate(seasons))
    list(enumerate(seasons, start=1))
    
    等价于:
        def enumerate(sequence, start=0):
            n = start
            for elem in sequence:
                yield n, elem
                n += 1
                
                
# globals()|locals()
    globals()函数：返回当前全局作用域内变量的字典
    locals()函数： 返回当前局部作用域内变量的字典
    
    dir(globals()['__builtins__'])，用来查看内置名称空间的名字。

## Python的名称空间
    名称空间就是存放名字与值绑定关系的地方。
    Python的三种命名空间：局部名称空间, 全局名称空间, 内置名称空间
    
    命名空间的查找顺序:
        局部名称空间 -> 全局名称空间 -> 内置名称空间
        
    命名空间的加载顺序：
        内置名称空间 -> 全局名称空间 -> 局部名称空间
        
    当一行代码要使用变量 x 的值时，Python会到名称空间去查找变量，按照如下顺序:
        1. 局部名称空间
            每个函数都有着自已的名称空间，叫做局部名称空间，它记录了函数的变量,包括 函数的参数和局部定义的变量
            这个命名空间在函数调用时被创建，在函数返回的时候被删除
            
            如果函数定义了一个局部变量 x，Python将使用这个变量，然后停止搜索
        
        2. 全局名称空间
            每个模块(py文件)拥有它自已的名称空间，叫做全局名称空间，它记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量
            在执行Python文件时，全局名称空间生效,当Python文件执行完毕时，全局名称空间失效。
            
            如果模块定义了一个名为 x 的变量，函数或类，Python将使用这个变量然后停止搜索
            
        3. 内置名称空间
            任何模块均可访问它，它存放着内置的函数如abs(), str()和异常。
            它在Python解释器启动的时候被创建，在解释器退出的时候才被删除。
            
            Python将假设 x 是内置函数或变量
            
        如果Python在这些名称空间找不到 x，它将放弃查找并引发一个 NameError 的异常，同时传 递 There is no variable named 'x' 这样一条信息
    
    

## Python作用域
    围绕Python的名称空间，其作用域一共分为两块：全局作用域、局部作用域
    
    1. 全局作用域：
        全局作用域由内置名称空间、全局名称空间两部分的名字与值之间的绑定关系组成
        其特点为：
            全局存活，全局有效，伴随Python文件执行始终
    2. 局部作用域：
        由局部名称空间的名字与值之间的绑定关系构成。
        其特点为：
            临时存活，局部有效。
            
    查看作用域的两个内置函数：globals()、locals()
    
    作用域关系，在函数定义时就已经确定，与调用位置无关：
        x = 23333
    
        def f1():
            def f2():
                print(x)
            return f2
        
        f = f1()
        
        def func():
            x = 123
            f()
        
        func()       #  23333  f()函数的作用域关系在定义时确定x = 23333（全局名称空间），与调用位置x=123（局部名称空间）无关

 ## globals|locals实列
    1. locals
        a = 1
        b = 2
        c = 3
        def fn(c,d):
            e = 300
            print("locals()返回：",locals())
        fn(100,200)
        
        输出值为：
            locals()返回： {'c': 100, 'd': 200, 'e': 300}
    
    2.globals
        如果我们想在局部变量中去访问全局变量c=3的值，我们就可以在
        局部变量内写入globals()["c"] ，即可访问全局变量中绑定的c的值
        
        a = 1
        b = 2
        c = 3
        def fn(c,d):
            e = 300
            print("globals()返回：",globals()["c"])
        fn(100,200)
        
        输出值为：
        globals()返回： 3
        
## 关键字global和nonlocal
    global      定义全局变量
    nonlocal    定义局部变量
    
    1. 在函数内部（局部名称空间）, 要想修改全局名称空间内变量的值需要使用关键字global声明
    
            x = 1
            def foo():
                global x
                x = 10
            foo()
            print(x)              # 10
            
    2. 在嵌套定义的函数中，要想修改上一级函数中（上一级局部名称空间）变量的值，需要使用关键字nonlocal进行声明。
       若上一级不存在该变量，则继续向上一级寻找，直到找到为止（仅限在函数内部）。找不到则报错。
        x = 1

        def foo():
            x = 2
            
            def foo2():
                nonlocal x
                x = 13213321
            foo2()
            print('foo:' + str(x))       #  13213321
   
    
        foo()
        print(x)           # 1
        
    3. global和nonlocal 结合
        def test():
        
            def do_local():
                spam = "local spam"
                
            def do_nonlocal():
                nonlocal spam
                spam = "nonlocal spam"
                
            def do_global():
                global spam
                spam = "global spam"
                
            spam = "test spam"
            
            do_local()
            print("after local assignment:", spam)       # 输出：test spam
            
            do_nonlocal()
            print("after nonlocal asssignment:", spam)   # 输出：nonlocal spam
           
            do_global()
            print("after global assignment:", spam)      # 输出：nonlocal spam
        
        
        test()
        print("in global scope:", spam)                  # 输出：global spa

# eval(expression[, globals[, locals]])
    expression参数会作为一个 Python表达式被解析求值并返回计算结果，使用 globals 和 locals 字典作为全局和局部命名空间
    不支持复杂的代码逻辑，例如赋值操作、循环语句等等
    globals 用于指定运行时的全局命名空间，类型是字典，缺省时使用的是当前模块的内置命名空间
    locals 指定运行时的局部命名空间，类型是字典，缺省时使用 globals 的值
    
    这两者不代表真正的命名空间，只在运算时起作用，运算后则销毁。
    
    1. 转换数据类型
        a = "{'test1': '1', 'test2': '2'}"
        b = eval(a)
        
    2. 执行表达式
        b = eval('data["name"]', {"data": {"name": "Python"}})
        b = eval('data["name"] + "-" + info["name"]', {"data": {"name": "Python"}}, {"info": {"name": "Mooc"}})
      
    globals和locals的应用：
        两者都缺省时，则遵循 eval 函数执行时的作用域
        
        x = 10
        def func():
            y = 20
            a = eval('x + y')                                    # 30
            b = eval('x + y', {'y': 1})                          # NameError: name 'y' is not defined  缺省时使用 globals 的值
            c = eval('x + y', {'x': 1, 'y': 2})                  # 3
            d = eval('x + y', {'x': 1}, {'y': 3})                # 4
            e = eval('x + y', {'x': 1, 'y': 2}, {'y': 3, 'z': 4}) # 4

# exec(object[, globals[, locals]])
    支持动态执行 Python 代码。功能更强大
    
    object 为代码块。
        一是它不能做表达式求值并返回出去，
        二是它可以执行复杂的代码逻辑，相对而言功能更加强大
    
    如果提供了 globals 参数，就必须是字典类型，而且会被用作全局和本地变量。
    如果提供了 locals 参数，则它可以是任何映射型的对象
    如果同时提供了 globals 和 locals 参数，它们分别被用作全局和本地变量。
    
    1. exec() 内外的命名空间是相通的
        变量由此传递出去，而不像 eval() 函数，需要一个变量来接收函数的执行结果。
        x = 1
        y = exec('x = 1 + 1')
        print(x)                    # 2
        print(y)                    # None
        
    2. exec() 函数内的变量是可以改变原有命名空间的
        1. my_dict 并未定义
            a = "my_dict = {'name': 'Python猫', 'age': 18}"
            exec(a)
            
            print(my_dict)
        
        2.更改data的值
        
            data = {"name": "Python"}
            exec('data["habby"] = "study"', {"data": data})
            
            print(data)   # {'name': 'Python', 'habby': 'study'}
            
    3. 多个条件
        def exec_example(m='Python', n='Basketball'):
    
            data = dict()
            exec(
                'data["name"]=m; data["hobby"]=n',
                {
                    "data": data,
                    "m": m,
                    "n": n
                },
                {}
            )
        
            return data
    
        print(exec_example())
        
    4. 执行函数
        class A(object):
            def __init__(self):
                self.cinema_url = "wwww.dianying.com"
        
            def get_cinema_info(self, cinema_code):
                return {
                    "cinema_code": cinema_code,
                    "cinema_name": " 测试",
                    "cinema_url": self.cinema_url
                }
        
            def exec_example(self, m='影院确认'):
                """使用闭包的方式执行get_cinema_info, 
                可直接引用外部的data,更加安全
                """
        
                data = {
                    "chain": "万达院线",
                    "cinema_code": 11047294
                }
        
                def get_cinema_info():
                    return {
                        "cinema_code": data["cinema_code"],
                        "cinema_name": " 测试",
                        "cinema_url": self.cinema_url
                    }
        
                exec(
                    'data["cinema_confirm"] = r;data["cinema_info"] = get_cinema_info()',
                    {
                        "data": data,
                        "r": m,
                        "get_cinema_info": get_cinema_info
                    },
                    {}
                )
        
                return data
        
            def exec_example_ex(self, m='院线确认'):
                """调用类方法更新cinema_info"""
        
                data = {
                    "chain": "万达院线",
                    "cinema_code": 11047294
                }
        
                exec(
                    'data["cinema_confirm"] = r;data["cinema_info"] = get_cinema_info("cinema_code")',
                    {
                        "data": data,
                        "cinema_code": data["cinema_code"],
                        "r": m,
                        "get_cinema_info": self.get_cinema_info
                    },
                    {}
                )
        
                return data
        
        print(A().exec_example_ex())
        
    5. 运行期的局部命名空间不可改变
        def foo():
            exec('y = 1 + 1\nprint(y)')
            print(locals())
            print(y)

        foo()
        
        result:
            2
            {'y': 2}
            Traceback (most recent call last)
            
            在运行期，exec() 函数动态地创建了局部变量 y ，然而由于 Python 的实现机制是“运行期的局部命名空间不可改变 ”，
            也就是说这时的 y 始终无法成为局部命名空间的一员，当执行 print() 时也就报错了
            
            若想把 exec() 执行后的 y 取出来的话，可以这样：z = locals()['y'] ，然而如果不小心写成了 y = locals()['y'] 则会报错

# isinstance()
    判断一个对象是否是一个已知的类型，类似 type()
    语法：
        isinstance(object, classinfo)
        
        如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例， 返回True
        如果object不是一个给定类型的的对象， 则返回结果总是False
        如果 classinfo 既不是类型，也不是类型元组或类型元组的元组，则将引发 TypeError 异常

    isinstance() 与 type() 区别：
        type() 不会认为子类是一种父类类型，不考虑继承关系。
        
        isinstance() 会认为子类是一种父类类型，考虑继承关系
    
    type: 用于查看对象的数据类型
    isinstance：用于判断两个类型是否相同推荐使用 isinstance()。
    
    a = 2
    print(isinstance (a,int))               #True
    print(isinstance (a,str))               #False
    print(isinstance (a,(str,int,list)))    #True


    class A:
        pass
    
    
    class B(A):
        pass
    
    
    print(isinstance(A(), A))               #  True
    print(type(A()) == A )                  #  True
    print(isinstance(B(), A))               #  True
    print(type(B()) == A)                   #  False
    

# callable()
    检查一个对象是否是可调用的 对于函数, 方法, lambda 函数式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True
    只要可以在一个对象的后面使用小括号来执行代码，那么这个对象就是callable对象

### 1.函数可调用
    def add(x, y):
        return x + y
    
    print(callable(add))            #True

### 2.类和类内的方法可调用, 类的实例不可调用
    class Demo(object):
    
        def get(self):
            return  True

    obj = Demo()
    print(callable(Demo))           #True
    print(callable(Demo.get))       #True
    print(callable(obj.get))        #True
    print(callable(obj))            #False

### 3.lambda表达式是可调用的
    f = lambda x,y : x + y
    print(f(2, 3))
    print(callable(f))              #True

### 4.整数，字符串，列表，元组，字典等等，都是不可调用
    print(callable(2))              #False
    print(callable('python'))       #False
    print(callable([1, 2, 3]))      #False
    print(callable({'a':1, 'b':2})) #False
    

# open() 文件处理
## Python文件操作流程：
    1. 得到文件对象   open()  
    2. 打开文件，得到文件描述符   file.fileno
    3. 对应文件驱动
    4. 操作硬件设备
## Python读取文件read() readline() readlines()的区别：
### 1.read(size)                  
    读取文件(读取size个字节,默认读取全部)
    一般小文件我们都采用read()，不确定大小就定个size 
### 2.readline(size)              
    读取一行   size参数的大小如果大于第一行的长度，并不会往下读取
### 3.readlines(size)             
    读取完文件,返回每一行所组成的列表  size存在从文件开头读到size参数长度所覆盖到的那一整行，尽管没覆盖到行末。
    如果文件太大 会造成MemoyError, 适合读取配置文件
    
    文本的内容为 '123\n456\n789\n\n' 如果size设为5
        read(5)会返回 '123\n4'
        readlines(5)会返回'123\n'
        readlines(5)返回 ['123\n', '456\n']

## with open
    with open(file_path, 'rb') as f:
    sha1Obj.update(f.read())

    with open(file_path, 'rb') as f:
        for line in f.readlines():
            print(line)
            
## 内置迭代方式
    在读取小文件时确实不会产生什么异常, 当文件特别大时，不建议使用read()或readlines()，建议使用内置迭代方式，如下
        f = open('test.log', 'r')
        for line in f:
        　　print(line)
        f.close()
    
    或者：
        with open(file_path, 'rb') as f:
        for line in f:
            print(line)
            
## Python写入方式:
    write(str): 将字符串写入文件
    writelines(data) 写多行到文件,参数为可迭代对象, argument must be str
    
    写入磁盘机制：
        1.主动调用close()或者flush()方法,写缓存同步到磁盘
        2.写入数据量大于或等于写缓存,写缓存同步到磁盘
    查看写缓存的大小：
        io.DEFAULT_BUFFER_SIZE
        
## 文件指针:
     f.tell()去检查当前文件指针的位置
     f.seek(offset,whence)
        offset代表文件的指针的偏移量，单位是字节bytes
        whence指针定位方式
        os.SEEK_SET:相对于文件起始位置 0
        os.SEEK_CUR:对于文件当前位置 1
        os.SEEK_END: 相对于文件结尾位置 2
        
## 打开文件后为什么要关闭：
    1. 将写缓存同步到磁盘中
    2. 系统中每个进程打开文件的个数是有限制的, 不主动关,就会产生占用
    3. 如果打开文件数到了系统限制，打开文件就会失败
    
## 读取大文件：
### 1.分块读取：将大文件分割成若干小文件处理，处理完每个小文件后释放该部分内存。用iter 和 yield来实现
    def read_in_chunks(filePath, chunk_size=1024*1024):
            file_object = open(filePath)
            while True:
                chunk_data = file_object.read(chunk_size)
                if not chunk_data:
                    break
                yield chunk_data

    if __name__ == "__main__":
        filePath = './path/filename'
        for chunk in read_in_chunks(filePath):
            pass
## With open()
    with语句打开和关闭文件，包括抛出一个内部块异常。for line in f文件对象f视为一个迭代器，会自动的采用缓冲IO和内存管理
            with open(file_path, 'r') as f:
                while True:
                    buf = f.read(1024)
                    if buf:
                        sha1Obj.update(buf)
                    else:
                        break

    with open()的优化：
        面对百万行的大型数据使用with open 是没有问题的，但是这里面参数的不同也会导致不同的效率。
        参数为”rb”时的效率是”r”的6倍。由此可知二进制读取依然是最快的模式

