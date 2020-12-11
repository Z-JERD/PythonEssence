# Python辅助工具

# 安装python第三方库的方法
## 1.pip安装
    pip install 库名
    
    指定版本安装：如flask
        pip install flask == 1.0.2
        pip install flask >= 1.0.2   必须大于1.0.2版本
        pip install flask <= 1.0.2 

## 2.whl安装
    在使用whl在之前，我们需要先在python中安装好wheel
    pip install wheel
    打开whl文件所在文件夹
    pip install xxx.whl(文件名称)
## 3.源码安装
    下载源码包后，里面有个setup.py的文件 打开setup.py文件所在文件夹
    python setup.py install
    
# 更换安装源
    常用的国内 PyPI 镜像列表：
    豆瓣 https://pypi.doubanio.com/simple/
    网易 https://mirrors.163.com/pypi/simple/
    阿里云 https://mirrors.aliyun.com/pypi/simple/
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    
    更换镜像安装库：如安装flask
    pip install -i https://pypi.doubanio.com/simple/ flask

# 查看版本
    1. 查看python和pip的版本
        python -V
        pip -V
        
        或者：
          python --version
          pip --version
          
    2. 查看第三方包的版本和文件位置
        import scipy
        scipy.__version__
        scipy.__file__
        
    3. 查看更多详情
        pip show scipy 
   
# pip的其他通途
          
    1. 搜索
        pip search flask
     
    2. 查询当前环境可升级的包
        pip list --outdated
        
    3. 查看一个包的详细内容
        pip show flask
        
    4. 导出当前项目所用到的依赖包
        pip install pipreqs 
        
        装好之后cmd到项目路径下
            pipreqs ./
        若显示 UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 213: illegal multibyte sequence
            pipreqs ./ --encoding=utf-8
    
    5. 导出python环境安装的所有安装包
        pip freeze > requirements.txt
    
    6. 安装依赖包
        pip install -r requirements.txt
        
        
# 安装虚拟环境
    1. pip install virtualenv
    
    2. 查看版本
        virtualenv --version
        
    3. 新建环境
        virtualenv env_django  
        
    4. 进入虚拟环境
        1. windows下
            进入env_django的Scripts目录中 输入 activate
          
            
        2.linux
            source env_django/bin/active　
            
    5. 退出虚拟环境
          退出 deactivate
          
          
# python内存监控工具
# 1. memory_profiler:按每行代码查看内存占用
        pip install -U memory_profiler

        from memory_profiler import profile
        @profile
        def my_func():
            a = [1] * (10 ** 3)
            b = [2] * (2 * 10 ** 2)
            del b
            return a

        if __name__ == '__main__':
            my_func()

# 2.guppy查看占用内存前十位变量
        直接打印出对应各种python类型（list、tuple、dict等）分别创建了多少对象，占用了多少内存
        pip install guppy

        from guppy import hpy
        mem = hpy()
        with open(file_path, 'r') as f:
                while True:
                    buf = f.read(1024)
                    if buf:
                        print(mem.heap())
                        sha1Obj.update(buf)
                    else:
                        break
                        
# 安装 gmpys 库：
## 参考文档：https://blog.csdn.net/dongyanwen6036/article/details/77183346   https://www.jianshu.com/p/37565f0ffdc8
    
## Windows：
        
        https://blog.csdn.net/x_yhy/article/details/83903367 
    
## Centos 安装gmpy库
        
        1、安装gmp开发包

            yum install -y gmp-devel

        2、安装python开发包

            yum install -y python-devel

        3、安装gmpy

            pip install gmpy
 
## Centos 安装gmpy2库   

### 创建目录        
    
    mkdir -p $HOME/src
    mkdir -p $HOME/static
    
    cd $HOME/src
    
### 1. gmp下载：
            
    1. 下载压缩包：wget https://gmplib.org/download/gmp/gmp-6.2.1.tar.bz2
    
    2. 解压： tar -jxvf gmp-6.2.1.tar.bz2
    
    3. cd gmp-6.2.1
    
    4. ./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic 
    
    5. make && make check && make install
            
### 2. mpfr下载： 
    
    1. wget https://www.mpfr.org/mpfr-current/mpfr-4.1.0.tar.bz2
    
    2. tar -jxvf mpfr-4.1.0.tar.bz2
    
    3. cd mpfr-4.1.0
    
    4. ./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic --with-gmp=$HOME/static
    
    5.  make && make check && make install
            
            
### 3. mpc下载：

        1. wget https://ftp.gnu.org/gnu/mpc/mpc-1.2.1.tar.gz
        
        2. tar -zxvf mpc-1.2.1.tar.gz
        
        3. cd mpc-1.2.1
        
        4. ./configure --prefix=$HOME/static --enable-static --disable-shared --with-pic --with-gmp=$HOME/static --with-mpfr=$HOME/static
        
        5. make && make check && make install
            
### 4.安装gmpy2：
        
    github项目：https://github.com/aleaxit/gmpy

    现在新的版本（2-2.1.0b1以上版本）在执行python setup.py build_ext --static=$HOME/static install

    会报错error: option --static must not have an argument
    
    解决法子1：

        找releases版本（2-2.1.0a1以下版本）来安装
        
        v=2-2.1.0a1
        cd $HOME/src
        wget https://github.com/aleaxit/gmpy/releases/download/gmpy${v}/gmpy${v}.tar.gz
        
        tar -zxvf gmpy2-2.1.0a1.tar.gz
        
        python setup.py build_ext --static=$HOME/static install
        
    解决方法2：
        
        python setup.py build_ext --static-dir=$HOME/static install
