# 内置模块

# string
    import string

    # 列举数字 0 - 9
        ret = string.digits

    # 列举小写字母
        ret  = string.ascii_lowercase
    
    #  列举大写字母
        ret = string.ascii_uppercase
    
    # 打印所有的大小写字母
        ret = string.ascii_letters

    # 列举所有标点符号
        ret = string.punctuation

    # 列举所有空白符
        ret = string.whitespace

    # 打印十六进制的字符
        ret = string.hexdigits
        
# Decimal

## Decimal类型的优点
    
    1. Decimal类型可以非常精确地在计算机中存储
    
      浮点数计算：1.1 + 2.2                   # 3.3000000000000003
      
      Decimal类型则不会出现这种情况:
        Decimal("1.1") + Decimal("2.2")      # Decimal('3.3')
      
    2. Decimal类型会自动保留小数点后面不需要的0
    
        浮点数计算：1.20 + 1.30                                      # 2.5
        
        Decimal：Decimal("1.20") + Decimal("1.30")                   # Decimal('2.50')
        
    3. Decimal类型可以根据需要自己设置小数点后精度。通过getcontext().prec = x
    
    缺点:
        精度提升的同时，肯定带来的是性能的损失。在对数据要求特别精确的场合（例如财务结算），这些性能的损失是值得的。
        但是如果是大规模的科学计算，就需要考虑运行效率了。毕竟原生的float比Decimal对象肯定是要快很多的
        
## Decimal运算

### 1. 传值：

    可以传递给Decimal整型或者字符串参数，但不能是浮点数据，因为浮点数据本身就不准确
    
    例: 
        Decimal(5.55)*100                          # Decimal('554.9999999999999822364316060')
        
        Decimal(1.1) + Decimal(2.2)                # Decimal('3.300000000000000266453525910')
        
    传入整数：
    
        Decimal(11.00)                             # Decimal('11')
        
        Decimal(2) + Decimal(3)                    # Decimal('5')
        
    传入str:
    
        Decimal(str(1.1)) + Decimal(str(2.2))      #  Decimal('3.3')
        
        Decimal(str(5.55))*100                     # Decimal('555.00')
            
### 2.  decimal & int & float 运算

    from decimal impoer Decimal
    
    float & float
            
            a, b = 1.2, 2.3
            print( a + b)                   # 3.5
            
            a, b = 1.2, 2.32
            print( a + b)                   # 3.5199999999999996
            
    int & float
            
            a, b = 2, 5.0
            print( a + b)                  # 7.0
            
            a, b = 2, 5.431
            print( a + b)                 # 7.431
            
    int & deciaml
            
            a, b = 1, Decimal(12)
            print( a + b)                 # 13
            
            a, b = 1, Decimal("12")
            print( a + b)                # 13
            
            a, b = 1, Decimal(12.05)
            print( a + b)                # 13.05000000000000071054273576
            
            a, b = 1, Decimal("12.05")
            print( a + b)                # 13.05
            
    flaot & deciaml
            a, b = 1.1, Decimal(12.05)
            TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'
            
            a, b = 1.0, Decimal(12.05)
            TypeError: unsupported operand type(s) for +: 'float' and 'decimal.Decimal'
 
### 3. Decimal 结果转化为string
    
    str(Decimal('3.40').quantize(Decimal('0.0')))                  3.4 <class 'str'>
    
### 4.浮点数据转换为Decimal类型

    Decimal.from_float(12.222)                       # Decimal('12.2219999999999995310417943983338773250579833984375')
    
##  精度 context
    
    可以用getcontext()函数得到当前运算环境的参数，直接打印 print (get context())
    
     Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, 
     flags=[Inexact, FloatOperation, Rounded], traps=[InvalidOperation, DivisionByZero, Overflow])
     
     prec精度为28，是默认值，可以通过getcontext().prec = 10这样来设置自己想要的精度
     rounding的规则是ROUND_HALF_EVEN
     
     Decimal(1)/Decimal(7)                             #  Decimal('0.1428571428571428571428571429')
     
     设置精度为6:
     
     decimal.getcontext().prec = 6
     
     Decimal(1)/Decimal(7)                                 # Decimal('0.142857')
     
## 四舍五入 保留小数

    from decimal import *

### 1. 未指定ROUND
    
        1. Decimal(50).quantize(Decimal('0.01'))           # Decimal('50.00')
        
        2. Decimal('7.325').quantize(Decimal('1.'))        # Decimal('7')
        
        3. Decimal('8.545').quantize(Decimal('0.01'))      # Decimal('8.54')
        
        4. Decimal('8.5451').quantize(Decimal('0.01'))     # Decimal('8.55')
        
        5. Decimal('8.535').quantize(Decimal('0.01'))      # Decimal('8.54')
        
        默认 ROUND 为: ROUND_HALF_EVEN
        
### 2.指定ROUND
    
    1. ROUND_UP：舍弃小数部分非0时，在前面增加数字
    
    2. ROUND_DOWN：舍弃小数部分，从不在前面数字做增加操作
    
    3. ROUND_CEILING：如果Decimal为正，则做ROUND_UP操作；如果Decimal为负，则做ROUND_DOWN操作；

    4. ROUND_FLOOR： 如果Decimal为负，则做ROUND_UP操作；如果Decimal为正，则做ROUND_DOWN操作；
    
    5. ROUND_HALF_DOWN：如果舍弃部分>.5，则做ROUND_UP操作；否则，做ROUND_DOWN操作；
    
    6. ROUND_HALF_UP：如果舍弃部分>=.5，则做ROUND_UP操作；否则，做ROUND_DOWN操作；
    
    7. ROUND_HALF_EVEN：如果舍弃部分左边的数字是奇数，则做ROUND_HALF_UP操作；若为偶数，则做ROUND_HALF_DOWN操作；
    
#### 1. ROUND_UP  & ROUND_DOWN

    Decimal('8.532').quantize(Decimal('0.01'), rounding="ROUND_UP")            # 8.54
    
    Decimal('8.530').quantize(Decimal('0.01'), rounding="ROUND_UP")            # 8.53
    
    Decimal('-8.532').quantize(Decimal('0.01'), rounding="ROUND_UP")           # -8.54
    
    Decimal('8.532').quantize(Decimal('0.01'), rounding="ROUND_DOWN")         # 8.53
     
    Decimal('-8.532').quantize(Decimal('0.01'), rounding="ROUND_DOWN")        # -8.53
    
#### 2.ROUND_CEILING & ROUND_FLOOR

    Decimal('8.532').quantize(Decimal('0.01'), rounding="ROUND_CEILING")       # 8.54
    
    Decimal('-8.532').quantize(Decimal('0.01'), rounding="ROUND_CEILING")      # -8.53
    
    Decimal('8.532').quantize(Decimal('0.01'), rounding="ROUND_FLOOR")         # 8.53
    
    Decimal('-8.532').quantize(Decimal('0.01'), rounding="ROUND_FLOOR")        # -8.54  
    
#### 3.ROUND_HALF_DOWN & ROUND_HALF_UP

    Decimal('8.535').quantize(Decimal('0.01'), rounding="ROUND_HALF_UP")       # 8.54
    
    Decimal('8.534').quantize(Decimal('0.01'), rounding="ROUND_HALF_UP")       # 8.53
    
    Decimal('8.535').quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN")     # 8.53
    
    Decimal('8.5350').quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN")    # 8.53
    
    Decimal('8.5351').quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN")    # 8.54
    
    Decimal('8.534').quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN")     # 8.53
    
    Decimal('8.536').quantize(Decimal('0.01'), rounding="ROUND_HALF_DOWN")     # 8.54

#### 4. ROUND_HALF_EVEN

    Decimal('8.535').quantize(Decimal('0.01'), rounding="ROUND_HALF_EVEN")     # 8.54
    
    Decimal('8.545').quantize(Decimal('0.01'), rounding="ROUND_HALF_EVEN")     # 8.54
    
    Decimal('8.5451').quantize(Decimal('0.01'), rounding="ROUND_HALF_EVEN")    # 8.55


## Python 序列化Decimal类型对象

    json 不能序列化 Decimal, datetime类型对象
    
    import json 
    
    from decimal import *
    
    dic = {"name": "jerd", "account": Decimal("500.56"))}
    
    json.dumps(dic)                                       #  TypeError: Object of type 'Decimal' is not JSON serializable
    
    解决方案：
        
        利用dumps的default, 遇到不能序列化的数据，转换成指定类型数据
        
        json.dumps(dic,default=str)                      # '{"name": "jerd", "account": "500.56"}'
    
    
# traceback 异常处理
##  python标准异常:http://www.runoob.com/python/python-exceptions.html

## try----except  

    def div(a, b):
        try:
            print(a / b)
    
        except ZeroDivisionError:
            # 发生异常则执行此处代码
            print("Error: b should not be 0 !!")
    
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            # 捕捉到了异常，但是又想重新引发它（传递异常），使用不带参数的raise语句即可
            raise
    
        else:
            # 没有异常则执行此处代码  （try里没有return执行，有return 不执行）
            print('Run into else only when everything goes well')
    
        finally:
            # 不论是否发生异常，均会执行 （无论try里是否有return均会执行）
            print('Always run into finally block.')

    
    
    1.except语句不是必须的，finally语句也不是必须的，但是二者必须要有一个，否则就没有try的意义了。
    
    2.except语句可以有多个，Python会按except语句的顺序依次匹配你指定的异常，如果异常已经处理就不会再进入后面的except语句。
    
    3.except语句可以以元组形式同时指定多个异常，参见实例代码。
    
    4.except语句后面如果不指定异常类型，则默认捕获所有异常
    
    5.如果要捕获异常后要重复抛出，请使用raise，后面不要带任何参数或信息。

## raise抛异常
    1. 在try---except中使用raise, 不需要使用参数
    2. 在非except中使用raise, 需要使用参数
    
    data = {
        'result':{
            'codes':23
        }
    }
    
    def active_throw():
    # 主动抛异常
        
        if data['result']['codes'] != 22:
            raise ValueError('code值有误')
            
    def throw_anomaly():
        
        try:
            codes = a['result']['code']
        except Exception as e:
           raise
        
## traceback.print_exc() 和 traceback.format_exc()
    查看错误详情,能清晰查看到是哪个文件,哪一行代码报的错
    
    1. traceback.print_exc()： 将结果直接给打印出来
        可以接受file参数直接写入到一个文件。比如
        traceback.print_exc(file=open('tb.txt','a+'))
    
    2. traceback.format_exc()：将错误以字符串的形式返回
    
    import traceback
   
    def catch_exceptions():
    
        try:
            codes = a['result']['code']
        except Exception as e:
            
            print(e)
            
            ee = traceback.format_exc()
    
            traceback.print_exc()
    
        """
         捕获异常：
            print(e)     'code'
    
        捕获异常后，查看详细的异常信息:
        traceback.format_exc()
              Traceback (most recent call last):
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 220, in catch_exceptions
                codes = a['result']['code']
            KeyError: 'code'
        捕获异常后，控制台显示详细的异常信息 traceback.print_exc()
        """
## catch_exceptions()
    实例中某个属性不存在时，调用该属性会抛出异常。使用getattr处理
        class Demo():
            
            def __init__(self):
                self.name = 'jerd'
    
            def get(self):
                return 66
    
        obj = Demo()
    
         age = obj.age
         
         """
          Traceback (most recent call last):
              File "C:/Users/86134/Desktop/demofile/wsgi-demo/demodb.py", line 249, in <module>
                age = obj.age
            AttributeError: 'Demo' object has no attribute 'age'
         """
           
    
        # 1.try捕获异常
            try:
                age = obj.age
            except AttributeError:
                age = 'default'
    
        # 2.getattr
            age1 = getattr(obj, 'age', 'default')
# inspect 模块提供了一些有用的函数帮助获取对象的信息 
    该模块提供了4种主要的功能：类型检查、获取源代码、检查类与函数、检查解释器的调用堆栈。
    
    import inspect
    import datetime

    def check(fn):
        def wrapper(*args,**kwargs):
            sig = inspect.signature(fn)
            params = sig.parameters
            values = list(params.values())
            for i, p in enumerate(args):
                if not isinstance(p,values[i].annotation):
                    assert False,'不符合条件的参数错误'
            for k, v in kwargs.items():
                if not isinstance(v,params[k].annotation):
                    assert False,'不符合条件的参数错误'
            return fn(*args,**kwargs)
        
        return wrapper
    
    @check
    def demo(a:int=None,b:bool=None,c:list=None,d:dict=None,e:datetime.datetime=None):
        print("========a:", a)
        print("========b:", b)
        print("========c:", c)
        print("========d:", d)
        print("========e:", e)

    demo(a=99,b=False, c=[1,2,3],d={"key":"test"},e=datetime.datetime.now())
    
    
    
# datetime模块
    datetime库定义了5个类:
        date类：表示日期的类
        time类：表示时间的类
        datetime类：表示时间日期的类
        timedelta类：表示两个datetime对象的差值；
        tzinfo类：表示时区的相关信息

        
## 1. datetime.date
    1. 创建自定义日期 个位数的月和日前面不要加0
        day = datetime.date(2019, 4, 15)
    2. 获取本地时间
        day = datetime.date.today()
    3. 日期属性
        day.year                        年
        day.month                       月
        day.day                         日
        day.weekday()                   获取星期几 获取星期几，0-6代表周一到周天
        day.isoweekday()                获取星期几，1-7代表周一到周天
## 2. datetime.time
    now_time = datetime.time(10, 21, 29,19999)
    时间属性：
        print(now_time.hour)
        print(now_time.minute)
        print(now_time.second)
        print(now_time.microsecond)

## 3. datetime.datetime
    自定义时间日期：
        dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
    获取本地当前时间日期
        dt = datetime.datetime.now()
    获取utc时间
        dt = datetime.datetime.utcnow()

    属性：
        dt.date()
        dt.time()
    
    查看日期属性：
        dt.year
    查看时间属性：
        dt.hour
            
## 4.datetime.timedelta 对时间进行运算操作
    interval = datetime.timedelta(days=7)         七天的时间间隔
    计算一周后的日期：
        future_day = day + interval

    计算两个时间的相隔天数：
        bday = date(2001, 1, 30)
        tday = date.today()
        interval = tday - bday

### 5.strptime 和 strftime
    
    strptime() : 输入的日期和时间是字符串，要处理日期和时间，str转换为datetime
        dt = '2019-4-2 10:01:34'
        cday = datetime.datetime.strptime(dt, '%Y-%m-%d %X')
        print(cday, type(cday), type(dt))

    strftime() : 后台提取到datetime对象后，要把它格式化为字符串显示给用户
        day = datetime.datetime.now()
        str_day = day.strftime('%Y-%m-%d %X')
        print(type(day), str_day, type(str_day))

## 6. datetime/timestamp转换
    在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
    记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp
    
    Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
    
    1. datetime类型转换为timestamp
         ret = datetime.datetime(2020, 4, 11, 12, 20).timestamp()
         print(ret, type(ret))
    
    2. timestamp转为datetime
        timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
        
        转本地时间：
            print(datetime.datetime.fromtimestamp(1586578800.0))
            
            2020-04-11 12:20:00
            
        转UTC时间
            print(datetime.datetime.utcfromtimestamp(1586578800.0))
            
            2020-04-11 04:20:00
    
## 7. 时区转换
    
    创建时区信息： timezone(timedelta(hours=8))
    
    先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
        utc_dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    # 转为北京时间
        bj_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
        print(bj_dt)
    
    # 转为东京时间
        tokyo_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
        print(tokyo_dt)
        
    # 北京时间转东京时间
        tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
     
    # 北京转utc时间
        utc_dt = bj_dt.astimezone(timezone(timedelta(hours=0)))
        
    输入日期为："2015-1-21 9:01:30", 时区信息如UTC+5:00 将其转换成timestamp,并转成北京时间
        utc_5 = datetime.datetime.strptime(dt_str, '%Y-%m-%d %X')
        utc_5 = utc_5.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=5)))
        utc_5_stamp = utc_5.timestamp()
        
        bj_dt = utc_5.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
        print(bj_dt)
        
# time模块

    1.时间有三种表示方式：
        1.1时间戳(给计算机看的）                            1970年1月1日之后的秒，即：time.time()

        1.2格式化的字符串(人能够看懂的时间)                  2016-12-12 10:10，  即：time.strftime('%Y-%m-%d')

        1.3结构化时间(操作时间的)                           元组   即：time.localtime()
                                                            共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)

    时间戳-->结构化时间
        time.gmtime(时间戳)                                 UTC时间，与英国伦敦当地时间一致
        time.localtime(时间戳)                              当地时间 不写参数默认当前时间的时间戳

    结构化时间-->时间戳　
        time.mktime(结构化时间)
        time_tuple = time.localtime(1500000000)
        time.mktime(time_tuple)

    结构化时间-->字符串时间
        time.strftime("格式定义","结构化时间")               结构化时间参数若不传，则默认当前时间
        例：
            time.strftime("%Y-%m-%d",time.localtime(1500000000))

            time.strftime("%Y-%m-%d %X")                      2019-04_02 10:24:25 <class 'str'>

    字符串时间-->结构化时间
        time.strptime(时间字符串,字符串对应格式)
        例：
            time.strptime("2017-03-16","%Y-%m-%d")              <class 'time.struct_time'>

            time.strptime("07/24/2017","%m/%d/%Y")


    time.time()         返回当前时间的时间戳
    time.sleep(0.3)     休眠  
# Arrow  第三方时间处理模块
# base64
    Base64是一种用64个字符来表示任意二进制数据的方法,是一种最常见的二进制编码方法,常用于在URL、Cookie、网页中传输少量二进制数据
    Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
    如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉

## 编码和解码
    1. 编码
        base_info = base64.b64encode('人生苦短, 我用python'.encode('utf-8'))   # b'5Lq655Sf6Ium55+tLCDmiJHnlKhweXRob24='
     
    2. 解码
        origin_info = base64.b64decode(b'5Lq655Sf6Ium55+tLCDmiJHnlKhweXRob24=')..decode("utf-8")
        
        # 人生苦短, 我用python
        
## urlsafe_b64
    由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
    
    encode_info = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')   # b'abcd++//'
    
    encode_info = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff') # b'abcd--__'
    
    decode_info = base64.urlsafe_b64decode(b'abcd++//')
    
# hashlib
    
    摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
    
    用处：1.密文存储 2.校验文件一致性

    
    摘要的内容必须是bytes类型
    
## MD5
    MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示

    1. 直接调用
        ret = hashlib.md5("人生苦短, 我用Python".encode('utf-8')).hexdigest()
        print(ret)                                      # 86b61bb2f18920c0de4859efbb62564b
    2. 分块调用 update
        1.
            md5_obj = hashlib.md5()
            md5_obj.update("人生苦短, 我用Python".encode('utf-8'))
            ret = md5_obj.hexdigest()
            print(ret)                                  # 86b61bb2f18920c0de4859efbb62564b
            
        2. 
            md5_obj = hashlib.md5()
            md5_obj.update("人生苦短, ".encode('utf-8'))
            md5_obj.update("我用Python".encode('utf-8'))
            ret = md5_obj.hexdigest()
            print(ret)                                   # 86b61bb2f18920c0de4859efbb62564b
            
    3. 静态加salt
         salt的值是固定的, 当两个用户使用相同的口令时,在数据库中，将存储两条相同的MD5值
         salt = "learn Python"

        ret = hashlib.md5(("人生苦短, 我用Python" + salt).encode('utf-8')).hexdigest()
        print(ret)                                      # c297762ec358f4bff6276a22530571e0
    
        md5_obj = hashlib.md5(salt.encode('utf-8'))
        md5_obj.update("人生苦短, 我用Python".encode('utf-8'))
        ret = md5_obj.hexdigest()                       # cd34872cbba220f3a570cc50089901cf
        print(ret)
        
    
    4. 动态加盐
        salt的值每次都随机产生
        
        salt = os.urandom(32)   # os.urandom(n) 随即产生n个字节的bytes，可以作为随机加密key
        
        salt = os.urandom(32)
        
        ret = hashlib.md5("人生苦短, 我用Python".encode('utf-8') + salt).hexdigest()
        print(ret)                                      # 8a9ca19456ef04f2c3313b7f29d85304


## SHA1
    
    调用SHA1和调用MD5完全类似
   
    SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
    比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
    
    import hashlib
    import os

    salt = os.urandom(32)
    ret = hashlib.sha1("人生苦短, 我用Python".encode('utf-8') + salt).hexdigest()
    print(ret) 
    
## 判断两个文件的一致性
    
    import os
    import hashlib


    def file_md5(filename):

        filesize = os.path.getsize(filename)    # 获取文件的大小

        with open(filename, 'rb') as f:
            md5_obj = hashlib.md5()
            while filesize:                      # 每次读10kb 知道filesize被读完
                content = f.read(1024 * 10)      
                md5_obj.update(content)
                filesize -= len(content)    

            file_md5 = md5_obj.hexdigest()

        return file_md5


    def judge(file1, file2):

        file1_md5 = file_md5(file1)
        file2_md5 = file_md5(file2)

        return file1_md5 == file2_md5

