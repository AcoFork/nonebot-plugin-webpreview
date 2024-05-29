# nonebot-plugin-webpreview
webpreview是一个适用于NoneBot的网页预览插件，使用playwright进行网页预览截图发送。所有代码均使用GPT构建

## 安装教程
 - 前往最新的Release，下载`webpreview.py`文件
 - 将下载的 `webpreview.xxx.py` 放入你的NoneBot的`plugins`文件夹即可
   
## 使用教程
 - 安装Playwright（如果有虚拟环境则进入虚拟环境）
   
   ```
   /// 安装依赖
   pip install playwright

   /// 下载浏览器
   playwright install
   ```
   
 - 启动
   

 - 直接发送带`HTTP` `HTTPS`的链接即可预览图片，如图

## WARNING
v0.3.0以下的版本使用老核心，需要自行配置，不建议使用。此README.md仅适用于最新版本的安装/使用教程

## 例图
![例图](eg.png)
