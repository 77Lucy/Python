import requests
import os

# API密钥和基础URL
API_KEY = "84d01f7733703bfe61ea8c7c339823a0"
BASE_URL = "https://api.weatherstack.com/current"

def get_weather(city):
    # 设置请求参数
    params = {
        "access_key": API_KEY,
        "query": city,
        "units": "m"  # 使用公制单位
    }

    try:
        # 发送GET请求
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # 如果请求失败，这将引发异常
        data = response.json()

        print(f"请求URL: {response.url}")  # 打印请求URL
        print(f"API Response: {data}")  # 打印完整的API响应

        # 检查API是否返回错误
        if "error" in data:
            return f"API错误：{data['error']['type']} - {data['error']['info']}"

        # 提取并返回天气信息
        current = data["current"]
        location = data["location"]
        weather_info = f"""
城市: {location['name']}, {location['country']}
温度: {current['temperature']}°C
体感温度: {current['feelslike']}°C
天气描述: {current['weather_descriptions'][0]}
湿度: {current['humidity']}%
风速: {current['wind_speed']} km/h
风向: {current['wind_dir']}
气压: {current['pressure']} mb
能见度: {current['visibility']} km
        """
        return weather_info

    except requests.exceptions.RequestException as e:
        return f"网络请求错误：{str(e)}\n请求URL：{response.url}"
    except KeyError as e:
        return f"数据解析错误：{str(e)}"
    except Exception as e:
        return f"未知错误：{str(e)}"

def main():
    while True:
        city = input("请输入您想查询天气的城市（输入'退出'结束程序）：")
        if city.lower() == '退出':
            print("谢谢使用，再见！")
            break
        
        weather_info = get_weather(city)
        print("\n天气信息：")
        print(weather_info)
        print("\n")

if __name__ == "__main__":
    main()
