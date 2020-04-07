# 装饰器, 迭代器, 生成器
## 参考文档：https://www.zhihu.com/question/20829330/answer/133606850


# 闭包
    闭包:内层函数对外层函数（非全局）变量的引用，该内层函数称为闭包函数
    函数内部定义的函数称为内部函数
    
    闭包函数的作用：
        保护内存，开启的内存空间,不会随着外部函数的结束而关闭.
        闭包中被内部函数引用的变量，不会因为外部函数结束而被释放掉，而是一直存在内存中，知道内部函数被调用结束
        
## 1.经典闭包函数
    def func():
        
        name="jerd"
        
        def inner():
            print(name)
        
        return inner
    
    func()()
    
## 2.判断是否为闭包函数的方法：函数名._closure_  结果有cell 就是闭包函数，结果为None，就不是闭包函数
       1. inner函数非闭包函数
           data = "人生苦短, 我用Python"
        
            def outer():
                def inner():
                    print(data)                 # data不是外部函数outer中的变量
        
                print(inner.__closure__)        # None
        
                return inner
        
            outer()()
        
       2. inner函数为闭包函数
            def outer():
                data = "人生苦短, 我用Python"
            
                def inner():
                    print(data)
            
                print(inner.__closure__)  # (<cell at 0x000001A2E065DB28: str object at 0x000001A2DF51A730>,)
            
                return inner


            outer()()

# 装饰器
    在不改变被装饰的函数及被装饰函数的执行方式下，给函数添加额外的功能. 用处：日志 本质就是闭包
    
    f1.__doc__          获取函数说明信息
    f1.__name__         获取函数名

    
## 1.简单装饰器
        import time
        from functools import wraps
      
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                start_time = time.time()
                ret = func(*args,**kwargs)
                end_time = time.time()
                print('----> 执行效率%s' % (end_time - start_time))
                return ret
            return inner

        @wrapper       # func = wrapper(func)
        def func():
            pass
        
        func()          # inner()
        
## 2.对装饰器加参数
    通过参数决定是否使用装饰器
    import time
    from functools import wraps
    
    def outter(flag):
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                if flag:
                    start_time = time.time()
                    ret = func(*args, **kwargs)
                    end_time = time.time()
                    print('----> %s 函数执行效率%s' % (func.__name__, end_time - start_time))
                else:
                    ret =  func(*args, **kwargs)
                return ret
    
            return inner
    
        return wrapper
    
    @outter(True)
    def func(*args):
        return args[0] + args[1]
    
    func(1,2)
 
## 3.多个装饰器装饰一个函数:离函数近的装饰器先执行
    from functools import wraps
    
    def wrapper1(func):  #func = f
        @wraps(func)
        def inner1():
            print('wrapper1 ,before func')
            func()                               #执行f()
            print('wrapper1 ,after func')
        return inner1
    def wrapper2(func):                          #func=inner1
        @wraps(func)
        def inner2():
            print('wrapper2 ,before func')
            func()                              #执行inner1（）
            print('wrapper2 ,after func')
        return inner2
    @wrapper2                                  # 此时 f=wrapper2(f) 相当于 inner1=wrapper2(inner1)  此时inner1=inner2
    @wrapper1                                  #离def f()近 先执行这个 此时f=inner1  再执行 @wrapper2
    def f():
        print('in f')
    f()                                        #相当于 inner2()
    

# 容器(container) 可迭代对象(iterable) 迭代器(iterator)

## 容器container
    
    容器是用来储存元素的一种数据结构,容器将所有数据保存在内存中,容器中的元素可以逐个地迭代获取
    
    在Python中典型的容器有：
        list、deque、set、dict、tuple、str
    
    通过判断一个对象是否包含某个元素来确定它是否为一个容器
        print(4 in [1,2,3])

## 可迭代对象iterable
    
    如果给定一个list或tuple,我们可以通过for循环来遍历这个list或tuple,这种遍历我们称为迭代（Iteration）
    
    迭代的概念:
        所谓迭代就是对可迭代对象调用__iter__方法,或者对迭代器调用__next__方法
    
    可迭代对象：
        实现了__iter__方法的对象都是可迭代对象。对可迭代对象调用__iter__方法会返回一个迭代器。
        定义可迭代对象，必须实现__iter__方法；
        然后可以对迭代器调用next()方法来获取对象的下一个元素
    
    判断某个对象是否为可迭代对象：
        dir(被测对象）会显示出所有的方法，如果有__iter__ 这个对象就叫可迭代对象
        li=[1,2,3]
        print('__iter__' in dir(li))
        
    大部分容器都是可迭代的,但是还有其他一些对象也可以迭代。例如,文件对象以及管道对象   
    
### 并非所有的容器都是可迭代对象
    定义⼀个容器MyList⽤来存放数据
    
     class MyList(object):

        def __init__(self):
            self.container = []

        def add(self, item):
            self.container.append(item)


    mylist = MyList()
    mylist.add(1)
    mylist.add(2)

    for num in mylist:
        print(num)
    TypeError: 'MyList'  object is not iterable
    
    MyList容器的对象也是不能迭代的
   
## 迭代器iterator
    
    迭代器协议：
        对象需要提供next方法，它要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代
    
    实现了__next__() (python2中实现 next())方法的对象都是迭代器
    定义可迭代对象：必须实现__iter__方法；
    定义迭代器：必须实现__iter__和__next__方法。
    
    迭代器有两个基本的方法：
        __iter__方法：返回迭代器对象本身
        __next__方法：返回迭代器的下一个元素   
                      next一次执行一次,如果超出范围，会报错
    
    优点： 
        1、提供一种统一的、不依赖与索引的取值方式，为for循环提供了依据 
        2、迭代器同一时间在内存中只有一个值—>更节省内存空间 
    缺点： 
        1、只能往后取，并且是一次性的 
        2、不能统计值的个数，即长度

### iter()和 next()
    
    迭代对象转换成迭代器：iterable.__iter__()或者iter(iterable)
        li = [1,2,3]
        print(type(li))  #<type 'list'>
        
        x = li.__iter__()
        或者:   x = iter(li)
        print(type(x))  #<type 'listiterator'>
    
    迭代器取值：
        iterator.__next__() 或者 next(iterator)
        
        print(x.__next__())
        或者: next(x)
       
    判断某个对象是否为可迭代对象还是迭代器：
        可迭代对象和迭代器都有__iter__,但迭代器有__next__,而可迭代对象没有
        print("__next__" in x.__dir__())            True
        print("__next__" in li.__dir__())           Flase
        
# for循环机制
## for循环内部实现原理
    1.能用for循环： str list dict tuple set  range 文件句柄
    
    2.for循环执行时的内部操作
        1.内部含有__iter__方法，先将可迭代对象转换成迭代器
        2.内部含有__next__方法，将值取出
        3.有异常处理的方法      迭代器中的值取完后，做了异常处理，避免了报错
    
    li = [1,2,3]
    for i in li:
        print(i)
    
    Python的for循环为什么可以遍历文件对象:
        f = open('/etc/passwd')
        for line in f:
            pass  
            
        在Python中，文件对象实现了迭代器协议，for循环并不知道它遍历的是一个文件对象，它只管使用迭代器协议访问对象即可

## while实现for循环    
    用while 查看和跳过报错语句
    1. 取值未作异常处理
        li = [1,2,3]
        s = li.__iter__()
        
        while True:    #把列表中元素输出完之后，继续执行，没有元素输出，就会报错
            print(s.__next__())  #print(next(s)) 效果一样
        
        结果 1 2 3  Traceback (most recent call last):  StopIteration
    
    2. 取值作异常处理
    li = [1,2,3]
    s = li.__iter__()
    while True:    #把列表中元素输出完之后，继续执行，没有元素输出，就会报错
        try:
            print(s.__next__())
        except  StopIteration:
            break  #结果 1 2 3

# 生成器
    为什么要引入生成器：
        之所以引入生成器，是为了实现一个在计算下一个值时不需要浪费空间的结构
        迭代器：  是在可迭代的基础上，加了一个next()方法。
        而生成器： 则是在迭代器的基础上(可以用for循环，可以使用next())再实现了yield
    
    Python有两种不同的方式提供生成器:
        1. 生成器函数：
            常规函数定义，但是，使用yield语句。yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行
        2. 生成器表达式：
            类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表
            
    生成器的性质：
        1. 具有yield关键字的函数都是生成器
        2. 生成器是一种特殊的迭代器，生成器自动实现了"迭代器协议"（即__iter__和__next__方法）不需要再手动实现两方法。
        3. 生成器在迭代的过程中可以改变当前迭代值(send)，而修改普通迭代器的当前迭代值往往会发生异常，影响程序的执行。
    
    大部分内置函数, 是使用迭代器协议访问对象的:
        求和的sum函数：
            sum(x ** 2 for x in range(4)) 
        而不用多此一举的先构造一个列表：
            sum([x ** 2 for x in xrange(4)])  
     
## 构建生成器
  
### 1.生成器表达式
        类似于列表解析式，区别在于生成式外面的是()而不是[]
        
            a = (i*i for i in [1, 2, 3])
        
        判断a对象类型:
            from collections import Iterable, Iterator, Generator

            print(isinstance(a, Iterable))                  True
            print(isinstance(a, Iterator))                  True
            print(isinstance(a,  Generator))                True
        
    
### 2.生成器函数
        
        生成器函数跟普通函数只有一点不一样,就是把 return 换成yield,其中yield是一个语法糖,内部实现了迭代器协议，同时保持状态可以挂起
        
        return:
            在一个生成器中，如果没有return，则默认执行到函数完毕；
            如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代.
        
        def f():
            yield 5
            print("--------")
            return
            yield 6
            print("=========")
        f = f()
        
        1.使用next取值
            print(f.__next__())             5
            print(f.__next__())             --------  异常：StopIteration  遇到return 就终止
          
        2.使用for循环取值
            for i in f:
                print(i)     5  --------

            for不报错的原因是内部处理了迭代结束的这种情况
        
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

## 生成器生命周期
    生成器在其生命周期中，会有如下四个状态:
        GEN_CREATED                 # 等待开始执行
        GEN_RUNNING                 # 解释器正在执行（只有在多线程应用中才能看到这个状态）
        GEN_SUSPENDED               # 在yield表达式处暂停
        GEN_CLOSED                  # 执行结束
        
    
    from inspect import  getgeneratorstate
    def mygen(n):
        now = 0
        while now < n:
            yield now
            now += 1
    
   
    if __name__ == '__main__':
        gen = mygen(2)
        print(getgeneratorstate(gen))           #  GEN_CREATED
    
        print(next(gen))
        print(getgeneratorstate(gen))           #  GEN_SUSPENDED
    
        print(next(gen))
        gen.close()                             #  手动关闭/结束生成器
        print(getgeneratorstate(gen))           #   GEN_CLOSED
 
 
 
        
### 3.send
    1.send和next的功能是一样的 g.send(None) 必须有参数
    2.给上一个yield整体发送一个返回值
    3.不能给最后一个yield发送返回值
    4.获取第一个值时，不能用send，只能用next     
    
    def func():
        print("=======")
        yield 222
        print("-------")
        count = yield 'cvx'
        print(count)
        yield 444
        yield 555
    g = func()
    
    print(g.__next__())            =======  222
    print(g.send(None))            -------  cvx
    print(g.send("+++++++"))       +++++++ 444
    print(g.send(None))            555
    
    def myList(num):  # 定义生成器
        now = 0  # 当前迭代值，初始为0
        while now < num:
            val = (yield now)  # 返回当前迭代值，并接受可能的send发送值；yield在下面会解释
            print(val)
            now = now + 1 if val is None else val  # val为None，迭代值自增1，否则重新设定当前迭代值为val
    my_list = myList(5)             # 得到一个生成器对象
    print(my_list.__next__())       # 0
    print(my_list.__next__())       #  None 1
    my_list.send(3)                 #1 3
    print(my_list.__next__())       # None 4

### yield from
    yield from 后面可以跟的式子有 生成器  元组 列表等可迭代对象以及range（）函数产生的序列
    yield from  generator ,实际上就是返回另外一个生成器
    相当于:
        for i in generator : yield i
        
    def generator1():
    item = range(7,9)
    for i in item:
        yield i

    def generator2():
        yield '========'
        yield from generator1()
        yield from ["---","*********","+++++++"]
        yield from range(1,3)

    next取值：
        obj = generator2()
        print(obj.__next__())            ========
        print(obj.__next__())            7
        print(obj.__next__())            8
        print(obj.__next__())            ---
    for 循环
        for i in generator2() :
            print(i)
            
        ========
        7
        8
        ---
        *********
        +++++++
        1
        2

### 基于面向对象实现迭代器
    class Fib(object):
        def __init__(self):
            self.num = 0

        def __iter__(self):
            print("=======")
            return self  # 实例本身就是迭代对象，故返回自己
    
        def __next__(self):
            self.num += 1
            if self.num >= 4:
                raise StopIteration()
            return self.num


    class Fub(object):
        def __init__(self):
            pass
    
        def __iter__(self):
            print("--------")
            for i in range(1,4):
                yield  i
                
        def __next__(self):
            print("==============")
    
    
    fibobject = Fib()
    fubobject = Fub()
    
    for i in fibobject:
        print(i)
        
    result:
        =======
        1
        2
        3
    
    for v in fubobject:
        print(v)
        
    result:
        --------
        1
        2
        3
        
   
    

        

## 生成器的高级应用              
### 1.生成器的操作
     1. 创建了一个生成器
        def func():
            print("==========")
            yield 222
            print("-----------")
            yield 444
        g = func()
        print(g.__next__())     ========== 222  此时指针停在 yield 222这行
        print(g.__next__())     -----------444  此时接着上次的位置
        print(g.__next__())     g中的值已经取完，无值可取 报错：StopIteration
        
     2. 创建了两个生成器：
        def func():
            print("==========")
            yield 222
            print("-----------")
            yield 444
        
        print(func().__next__())  ===== 222 此时指针停在 yield 222这行
        print(func().__next__())  ===== 222
    
    
    
    3. 生成器关闭
        def func():
            for i in range(1000):
                yield "衣服%s" % i


        g = func()
        for i in range(3):
            print(g.__next__())             # 衣服0 衣服1 衣服2
    
        g.close()
        
### 2.send
    1.send和next的功能是一样的 g.send(None) 必须有参数
    2.给上一个yield整体发送一个返回值
    3.不能给最后一个yield发送返回值
    4.获取第一个值时，不能用send，只能用next     
    
    def func():
        print("=======")
        yield 222
        print("-------")
        count = yield 'cvx'
        print(count)
        yield 444
        yield 555
    g = func()
    
    print(g.__next__())            =======  222
    print(g.send(None))            -------  cvx
    print(g.send("+++++++"))       +++++++ 444
    print(g.send(None))            555
    
    def myList(num):  # 定义生成器
        now = 0  # 当前迭代值，初始为0
        while now < num:
            val = (yield now)  # 返回当前迭代值，并接受可能的send发送值；yield在下面会解释
            print(val)
            now = now + 1 if val is None else val  # val为None，迭代值自增1，否则重新设定当前迭代值为val
    my_list = myList(5)             # 得到一个生成器对象
    print(my_list.__next__())       # 0
    print(my_list.__next__())       #  None 1
    my_list.send(3)                 #1 3
    print(my_list.__next__())       # None 4
        
### 3. sum应用
    生成器的好处是延迟计算，一次返回一个结果。也就是说，它不会一次生成所有的结果，这对于大数据量处理，将会非常有用

    sum([i for i in range(10 ** 11)])              # 非常耗内存
    sum(i for i in range(10 ** 11))                # 几乎不占内存
            
### 4. 生成器只能遍历一次
    def get_province_population(filename):
        with open(filename) as f:
            for line in f:
                yield int(line)


    gen = get_province_population('data.txt')
    all_population = sum(gen)

    for population in gen:
        print(population / all_population)

    执行上面这段代码，将不会有任何输出，这是因为，生成器只能遍历一次。在我们执行sum语句的时候，就遍历了我们的生成器，
    当我们再次遍历我们的生成器的时候，将不会有任何记录

# 基于面向对象实现迭代器
    class Fib(object):
        def __init__(self):
            self.num = 0

        def __iter__(self):
            print("=======")
            return self  # 实例本身就是迭代对象，故返回自己
    
        def __next__(self):
            self.num += 1
            if self.num >= 4:
                raise StopIteration()
            return self.num


    class Fub(object):
        def __init__(self):
            pass
    
        def __iter__(self):
            print("--------")
            for i in range(1,4):
                yield  i
                
        def __next__(self):
            print("==============")
    
    
    fibobject = Fib()
    fubobject = Fub()
    
    for i in fibobject:
        print(i)
        
    result:
        =======
        1
        2
        3
    
    for v in fubobject:
        print(v)
        
    result:
        --------
        1
        2
        3
        
 
# yield from
    yield from 后面可以跟的式子有 生成器  元组 列表等可迭代对象以及range（）函数产生的序列
    yield from  generator,实际上就是返回另外一个生成器
    相当于:
        for i in generator : yield i
        
       def generator1():
            item = range(7,9)
            for i in item:
                yield i

       def generator2():
            yield '========'
            yield from generator1()
            yield from ["---","*********","+++++++"]
            yield from range(1,3)
    
       
        for i in generator2() :
            print(i)
            
        ========
        7
        8
        ---
        *********
        +++++++
        1
        2
        
## yield from:拼接可迭代对象
        astr = 'ABC'
        alist = [1,2,3]
        adict = {"name":"wangbm","age":18}
        agen = (i for i in range(4,8))
        
        
        def gen(*args, **kwargs):
            for item in args:
                yield from item
        
        new_list = gen(astr,alist,adict,agen)
        print(list(new_list))
        
#### yield from:处理异常
        # 子生成器
        def average_gen():
            total = 0
            count = 0
            average = 0
            while True:
                new_num = yield average
                if new_num is None:
                    break
                count += 1
                total += new_num
                average = total/count
            return total,count,average
        
        def proxy_gen():
            while True:
                 yield from average_gen()
        
        # 调用方
        def main():
            calc_average = proxy_gen()          #自动做了异常处理
            # calc_average = average_gen()      #抛出异常
            next(calc_average)            
            print(calc_average.send(None))
        
        
        if __name__ == '__main__':
            main()

        
#### yield from :构建双向通道
        1、调用方：调用委派生成器的客户端（调用方）代码
        2、委托生成器：包含yield from表达式的生成器函数
        3、子生成器：yield from后面加的生成器函数
        
        # 子生成器
        def average_gen():
            total = 0
            count = 0
            average = 0
            while True:
                new_num = yield average
                count += 1
                total += new_num
                average = total/count
        
        # 委托生成器
        def proxy_gen():
            while True:
                yield from average_gen()
        
        # 调用方
        def main():
            calc_average = proxy_gen()
            next(calc_average)            # 预激下生成器
            print(calc_average.send(10))  # 打印：10.0
            print(calc_average.send(20))  # 打印：15.0
            print(calc_average.send(30))  # 打印：20.0
        
        if __name__ == '__main__':
            main()
            
        委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。
        调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方
        
        结束子生成器
        from inspect import getgeneratorstate
        # 子生成器
        def average_gen():
            total = 0
            count = 0
            average = 0
            while True:
                new_num = yield average
                if new_num is None:
                    break
                count += 1
                total += new_num
                average = total/count
        
            # 每一次return，都意味着当前协程结束。
            return total,count,average
        
        # 委托生成器
        def proxy_gen():
            while True:
                average_gener = average_gen()
                total, count, average = yield from average_gener
                print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
                print(getgeneratorstate(average_gener))
        
        # 调用方
        def main():
            calc_average = proxy_gen()
            next(calc_average)            # 预激协程
            print(calc_average.send(10))  # 打印：10.0
            print(calc_average.send(20))  # 打印：15.0
            print(calc_average.send(30))  # 打印：20.0
            calc_average.send(None)      # 结束协程
            print(getgeneratorstate(calc_average))
            # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程
        
        if __name__ == '__main__':
            main()
    


   
        
  

# 生成器经典应用（读取只有一行500G文件）
## 参考文档：https://blog.csdn.net/qq_34979346/article/details/83934181
    一个文件 大概有500G，并且只有一行，行之间有分隔符，需要把文件内的数据一行一行的读取出来
    
    def readfile(f, symbol, size=2048):
        """
        :param f:
        :param symbol:
        :param size:默认块大小：2KB
        :return:
        """
        buf = ""
        while True:
            while symbol in buf:                        # 判断 分隔符是否在暂存数据
                position = buf.index(symbol)            # 用了index 方法并且返回分隔符的下标
                yield buf[:position]                    # 取分隔符前面的值保存在生成器
                
                buf = buf[position+len(symbol):]        # 取过值也更新buf，删除前面取的值加上分隔符
            
            content = f.read(size)                      # 一次读取的字符   
            if not content:                             # 如果取不到值了，就用这个结束循环
                yield buf                               # 最后一个分隔符后边的值也保存在生成器里
                break
            buf += content
            
    with open("demo.txt") as f:
        for line in readfile(f, "|", 2048 * 5):
            print(line)

