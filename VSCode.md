# 基本配置：

    1. 配置语法提示：
        
        pip install flake8
        
        settings.json中添加："python.linting.flake8Enabled": true,
        
    2. 自动补全代码：
        
        "python.autoComplete.addBrackets": true,
        
    3. 滑轮控制代码大小：

        "editor.mouseWheelZoom": true,
        
    4. 设置自动保存：

        "files.autoSave": "afterDelay",
        
    5. 折叠代码

        要操作光标所在文件中的所有代码块：

            折叠所有 Ctrl+K+0（零）
            展开所有 Ctrl+K+J
        
        仅仅操作光标所处代码块内的代码：

        折叠 Ctrl+Shift+[
        展开 Ctrl+Shift+]
        
        
# VSCODE 同步代码到远程服务器

## 1. VSCODE 安装 SFTP插件

## 2. 创建sftp配置

    使用 ctrl+shift+p 快捷键调出输入框，选择 SFTP:Config 回车

    会在 .vscode 目录下创建一个 sftp.json 配置文件，配置如下

    {
        "name": "My Server",
        "host": "10.110.30.144",
        "protocol": "sftp",
        "port": 22,
        "username": "root",
        "password": "123456789",
        "remotePath": "/root/remotewk",     # 服务器文件路径
        "uploadOnSave": true,
        "syncMode": "update",
        "ignore": [            
            "**/.vscode/**",
            "**/.git/**",
            "**/.DS_Store"
        ]
    }

## 3. 基本操作：


    本地文件和服务器上有相同文件, 在本地修改后, 会自动同步到服务器上

    
### 1. 上传或拉取单个文件：

        在当前文件, 鼠标点击右键, 选择Upload或者Download

    本地新增文件，点击Upload上传到服务器上

### 2. 上传当前文件夹所有文件到服务器: 

        ctrl+shift+p 快捷键调出输入框

        输入：SFTP:Upload Project

### 3. 从服务器拉取代码到本地：

       ctrl+shift+p 快捷键调出输入框
       输入：SFTP: Sync Remote -> Local
