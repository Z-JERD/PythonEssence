# Pycharm永久激活参考文档：https://segmentfault.com/a/1190000021278253

## 1.颜色设置
    
    快捷键 Ctrl+Alt+S 打开 PyCharm 的设置面板
    Editor—>Color Scheme—>General选择你喜欢的颜色主题
    
## 2.修改界面中字体样式
    
    快捷键 Ctrl+Alt+S 打开设置面板
    Appearance & Behavior—>Appearance—>Use custom font
    
## 3.修改代码字体大小
    
    快捷键 Ctrl+Alt+S 打开设置面板
    Editor—>General—>Mouse—>Change font size
    
## 4.快速注释&取消注释
    
    ctrl+/ 快捷键进行注释
    再次快捷键，取消注释 
   
## 5.快速换行
    
    快捷键shift+enter可以快速换行，与换行位置代码缩进保持一致
    
## 6.快速定位到错误行： Shift + F2

## 7.快速查看最近的修改： Alt + Shift + C

## 8.代码性能分析

    Run -> Profile '程序' ，即可进行性能分析
    点击 Call Graph（调用关系图）界面直观展示了各函数直接的调用关系、运行时间和时间百分比
    
## 9. 格式化代码：Reformat Code 
    
    快捷键是 Ctrl + Alt + L
    
## 10.折叠代码&展开代码
    
    所有代码折叠：ctrl+alt+-
    
    所有代码展开：ctrl+alt++
    
    折叠某一层：ctrl+-
    
    展开某一层：ctrl++
    
    折叠个别代码：选中想折叠的代码，Ctrl+.
    
    
## 11.源码文档，快速预览
    
    1. Ctrl + 鼠标左键       可以实现函数跳转查看源码
   
    2. Ctrl + shift + i     在当前页面展示源代码
    
    3. Ctrl + q             当前页面就可以快速预览 接口文档
    
## 12. 快速给列出有哪些地方调用某个类/方法
    
    鼠标点击类/方法后，按下快捷键：Ctrl+Alt+F7

## 13. 代码静态审查
    
    PyCharm的Inspect Code提供了代码静态审查功能，可以检测出语法错误，不符合PEP8的代码以及提供建议
    
    1.在需要审查的文件夹或文件点击右键

    2.点击Inspect Code打开代码审查界面
    
    3.Inspect Code界面包括两部分：左边列出审查结果，右边操作界面。点击右边的Reformat file 按钮可以自动格式化代码使之符合PEP8规范。

## 14. 精准定位

    1. 精准定位到文件：Ctrl+Shift+N
    
    2. 精准定位到类：Ctrl+N
    
    3. 精准定位到符号：类的所有成员（函数、变量等）都可以称之为符号 Ctrl+Alt+Shift+N
    
    4. 精准定位到某行：Ctrl+G
    
 ## 15. 快速记录下当前的思绪状态
    
    1. TODO: 
        使用PyCharn 的 TODO 功能快速记录下当前的思绪状态，以及下一步要做的事情,
        使用方法跟注释差不多，但要以 TODO 开头。然后，查看全局项目中的所有 TODO事项：Alt+6。

    2. FIXME
        比较紧急的 BUG，可以使用类似 TODO 的标记 — FIXME来区分紧急程度
        
        
## 16. 作用域批量更改

    PyCharm 的 Refactor 功能，它会自动匹配作用域，做到批量更改
    先选中你的变量，然后使用快捷键 Shift+F6，就可以直接重命名了
    
    如：只将demo_func中的test_name 改为demo_name
    
        test_name = 'python'
    
    
        def demo_func(test_name):
            time.sleep(1)
            name1 = test_name
            name2 = test_name
            name3 = test_name
         
## 17.误删文件/恢复历史文件
    
    1. 恢复误删的文件
        项目目录里，点击右键，有个 Local History 的选项，再点击子选项 Show History，可以看到有个记录板。
        如果想恢复删除的文件，就在删除的记录项点击右键，选择 Revert 即可恢复
    
    2. 恢复文件内容
        对代码进行回滚，在需要回滚的py文件的空白处右键点击，然后在弹出的选项卡中选择Local History>>Show History
        对话框中包含三栏，左侧是代码的各个历史版本，中间一栏是在左侧栏中被选中的某个历史版本，最右侧一栏是代码的当前版本
        代码的回滚只需在左侧栏中右键选中要回滚的版本，然后在弹出的小对话框中选择Revert即可
        
             
## 18. pycharm远程上传文件到Linux
    
    参考文档：https://blog.csdn.net/z_yong_cool/article/details/80716020
    
    1. 在PyCharm中打开SFTP配置面板，路径为Tools => Deployment => Configuration
    
    2. 配置Connection参数设置，填写远程服务器域名或者IP地址及用户名密码后，点击Test按钮进行连接测试，另外可以点击Autodetect按钮自动关联root path：
    
    3.配置Mappings参数设置，进行本地项目路径和远程服务器项目路径的关联：（圈红的是上传到Linux上的哪个文件下）
    
    4. 点击OK后，即可通过右键点击待操作文件进行本地、远程的Upload、Download及Sync


 