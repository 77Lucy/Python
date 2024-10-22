import requests

def get_location_info(place_name):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "YourAppName/1.0"  # 请替换为您的应用名称
    }

    response = requests.get(base_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            location = data[0]
            return {
                "名称": location.get("display_name"),
                "纬度": location.get("lat"),
                "经度": location.get("lon")
            }
        else:
            return None
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None

def main():
    place = input("请输入您想查询的地点：")
    result = get_location_info(place)
    
    if result:
        print("\n地点信息：")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("未找到该地点的信息。")

if __name__ == "__main__":
    main()
