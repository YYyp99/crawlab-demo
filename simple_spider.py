import requests
import time
from datetime import datetime

def crawl():
    """
    简单爬虫演示 - 抓取一个网页并输出基本信息
    """
    url = "https://httpbin.org/get"
    
    print(f"[{datetime.now()}] 开始爬取: {url}")
    
    try:
        # 发送请求
        response = requests.get(url)
        
        # 检查响应状态
        if response.status_code == 200:
            # 解析返回的JSON
            data = response.json()
            
            print(f"请求成功! 状态码: {response.status_code}")
            print(f"服务器响应时间: {response.elapsed.total_seconds():.3f}秒")
            print(f"返回数据大小: {len(response.text)} 字节")
            print(f"返回的IP: {data.get('origin', 'unknown')}")
            print(f"请求头信息: {data.get('headers', {})}")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    
    except Exception as e:
        print(f"发生错误: {e}")
    
    print(f"[{datetime.now()}] 爬取完成")

# 主程序入口
if __name__ == "__main__":
    crawl()
