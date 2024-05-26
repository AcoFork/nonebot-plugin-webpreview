import asyncio
import base64
from nonebot import on_message
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment
from pyppeteer import launch

# Chrome 可执行文件路径
CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# 创建一个事件响应器，用于处理消息
preview_webpage = on_message()

@preview_webpage.handle()
async def handle_preview(event: Event):
    # 获取用户发送的消息
    user_msg = str(event.get_message()).strip()

    # 检查消息是否以 "http://" 或 "https://" 开头
    if not user_msg.startswith(("http://", "https://")):
        return

    # 启动浏览器
    browser = await launch(executablePath=CHROME_PATH, headless=True)
    page = await browser.newPage()

    try:
        # 转到用户提供的网址
        await page.goto(user_msg)

        # 等待5秒
        await asyncio.sleep(5)

        # 截取整个网页的屏幕截图
        screenshot_data = await page.screenshot(fullPage=True, encoding="base64")

        # 发送截图
        await preview_webpage.send(MessageSegment.image(f"base64://{screenshot_data}"))
    except Exception as e:
        await preview_webpage.send(f"无法预览网页：{str(e)}")
    finally:
        # 关闭浏览器
        await browser.close()
