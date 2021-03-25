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
