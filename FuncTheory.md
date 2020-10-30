# python函数的值传递和引用传递

## 参考文档：https://blog.csdn.net/haoxun10/article/details/104704617

## 变量地址
### 1. 不可变类型
    
    不可变类型int和较短的字符串，无论创建多少个不可变类型，只要值相同，都指向同个内存地址
    
    Python对int类型和较短的字符串进行了缓存，无论声明多少个值相同的变量，实际上都指向同个内存地址
    
        d1 = 234                       # id(d1)  1539476224
        
        d2 = 234                       # id(d2)  1539476224
        
        d2 = 456                       # id(d2)  2424981044048
        
        d3 = d1                        # id(d3)  1539476224
        
        a = "zhaogaungfeixuexipython"   # id(a)   2424981281720
        
        b = "zhaogaungfeixuexipython"   # id(b)   2424981281720
        
    浮点型：两个相同值的浮点型变量，并不是指向同个内存地址
        
        f1 = 7.89                      #  id(f1)     2424960847664
        
        f2 = 7.89                      # id(f2)      2424960847760
        
        f3 = f2                        # id(f3)      2424960847760
        
        f4 = 12.1111                   #  id(f4)     2424981332520
        
        f4 = 9.1111                    #  id(f4)     2424981332592
        
        f4 = 12.1111                   #  id(f4)     2424981332424
        
    元祖：变量赋新值后，指向改变，再修改为原来的值，指向重新指回原来的地址
        
        t1 = (1, 2, 3)                 # id(t1)      2424981120632
        
        t2 = (1, 2, 3)                 # id(t2)      2424981002568
        
        t1 = (1, 2, 3, 4)              # id(t1)      2424981342392
        
        t1 = (1, 2, 3)                 # id(t1)      2424981120632
        
        
### 2. 可变类型：存在多个值相同的变量时，指向不同的内容地址
    
    l1 = [1, 2, 3]                    # id(l1)      2424981381768
    
    l2 = [1, 2, 3]                    # id(l2)      2424981364552
    
    l3 = l1                           # id(l3)      2424981381768
    
    l1 = [1, 2, 3, 5]                 # id(l1)      2424981170888
    
    l1 = [1, 2, 3]                    # id(l1)      2424981403976
    

## 值传递：
    
    传递过来的是一个数据的副本；修改副本对原件没有任何影响。
    
## 引用传递:
    
    传递过来的，是一个变量的地址；通过地址可以操作同一份原件
    
## 示例：
### 1. 参数为不可变类型

    def demo(param):
    
        print(param, id(param))              # PythonDemo 2126674892272
        
        param + "Python"

        print(param, id(param))             # PythonDemo 2126674892272
    
        param = "Python"
    
        print(param, id(param))              # Python 2126672000592
    
    
    data = "PythonDemo"
    
    print(data, id(data))                    # PythonDemo 2126674892272
    
    demo(data)
    
    print(data, id(data))                    # PythonDemo  2126674892272


### 2. 参数为可变类型

    def demo(param):
    
        print(param, id(param))              # [1, 2, 3, 4] 1326743712008
    
        param.append(5)
    
        print(param, id(param))              # [1, 2, 3, 4] 1326743712008
    
    
    data = [1, 2, 3, 4]
    
    print(data, id(data))                    # [1, 2, 3, 4, 5] 1326743712008
    
    demo(data)
    
    print(data, id(data))                    # [1, 2, 3, 4, 5] 1326743712008
    
 
## 总结：
    
    形参的地址和实参的地址是同一指向, 在python中，只有引用传递
 
## 详解  
### 变量与对象
    
    Python 中一切皆为对象，数字是对象，列表是对象，函数也是对象，任何东西都是对象。
    
    变量是对象的一个引用（又称为名字或者标签），对象的操作都是通过引用来完成的。
    
    a = []
    
    []是一个空列表对象，变量 a 是该对象的一个引用
    
### 赋值

    在 Python 中，「变量」更准确叫法是「名字」，赋值操作 = 就是把一个名字绑定到一个对象上。就像给对象添加一个标签
    
    a = 1        整数 1 赋值给变量 a 就相当于是在整数1上绑定了一个 a 标签
    
    a = 2        整数 2 赋值给变量 a，相当于把原来整数 1 身上的 a 标签撕掉，贴到整数 2 身上
    
    b = a        把变量 a 赋值给另外一个变量 b，相当于在对象 2 上贴了 a，b 两个标签，通过这两个变量都可以对对象 2 进行操作
    
 
 ### 函数中的默认值指向同一地址
#### 1. 默认值不可变
    def demo(param, args1=3):
    
        print(param, id(param))
        
        print(args1, id(args1))
    
    
    data = "PythonDemo"
    
    data_1 = "Python"
    
    print(data, id(data))           # PythonDemo    2489450665456
    
    print(data_1, id(data_1))       # Python        2489418741328
    
    demo(data)                      # PythonDemo    2489450665456
                                    # 3             1539468832
    
    demo(data_1)                    # Python        2489418741328
                                    # 3             1539468832
                                    
                                    
    def demo(param, args1=[]):

    print(param, id(param))

    print(args1, id(args1))

#### 2. 默认值可变

     def demo(param, args1=[]):
        
            print(param, id(param))
            
            print(args1, id(args1))
    
    data = "PythonDemo"
    
    data_1 = "Python"
    
    print(data, id(data))           # PythonDemo    1525458441712
    
    print(data_1, id(data_1))       # Python        525426452048
    
    demo(data)                      # PythonDemo    1525458441712
                                    # []            1525458432264
    
    demo(data_1)                    # Python        1525426452048
                                    # []            1525458432264
                                    
#### 3. 传递默认参数

    def demo(param, args1=3):
    
        print(param, id(param))
    
        print(args1, id(args1))
    
    
    data = "PythonDemo"
    
    data_1 = "Python"
    
    print(data, id(data))           # PythonDemo    2329930208752
    
    print(data_1, id(data_1))       # Python        2329927317072
    
    demo(data, 4)                   # PythonDemo    2329930208752
                                    # 4             1539468864
    
    demo(data_1, 5)                 # Python        2329927317072
                                    # 5             1539468896
                                    
### 默认值为可变对象示例

    def bad_append(new_item, a_list=[]):
    
        print(a_list, id(a_list))
    
        a_list.append(new_item)
    
        return a_list
    
    
    ret = bad_append("one")                          # [] 1652747796424
    
    print(ret)                                      
                                                     # ['one']
    
    ret = bad_append("two")                          # ['one'] 1652747796424
    
    print(ret)                                       # ['one', 'two']
    
    
    修改后：
        
        def good_append(new_item, a_list=None):
        
            print(a_list, id(a_list))
            
            if a_list is None:
            
                a_list = []
            
            print(id(a_list))
            
            a_list.append(new_item)
            
            return a_list
        
        
        ret = good_append("one")                      # None 1539024080   2379147116488
        
        print(ret, id(ret))                           # ['one'] 2308680187848
        
        ret = good_append("two")                      # None 1539024080    2308680216840
        
        print(ret, id(ret))                           # ['two'] 2308680216840
        
