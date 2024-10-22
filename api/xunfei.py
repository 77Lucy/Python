import requests
import json

def get_response(user_content):
    url = "https://spark-api-open.xf-yun.com/v1/chat/completions"
    data = {
        "max_tokens": 500,
        "top_k": 4,
        "temperature": 0.5,
        "messages": [
            {
                "role": "system",
                "content": "你是一个喜欢红楼梦的学者,回答时风格要模仿红楼梦里林黛玉说话的语气，用词精致"
            },
            {
                "role": "user",
                "content": user_content  # 使用传入的用户提问内容
            }
        ],
        "model": "generalv3.5"
    }
    data["stream"] = True
    header = {
        "Authorization": "Bearer FfAhHFJGShMeVjZrbRzi:qEiKhpvIcyGnBbNfDPYW"
    }
    response = requests.post(url, headers=header, json=data, stream=True)

    # 流式响应解析示例
    response.encoding = "utf-8"
    for line in response.iter_lines(decode_unicode="utf-8"):
        if line:
            try:
                # 解析JSON行
                json_data = json.loads(line.lstrip("data: "))
                # 提取文本内容
                if "choices" in json_data:
                    delta = json_data["choices"][0].get("delta", {})
                    content = delta.get("content", "")
                    print(content, end='')  # 逐行输出内容
            except json.JSONDecodeError:
                continue

if __name__ == '__main__':
    user_question = input("请输入您的问题：")  # 从用户输入获取提问内容
    print("\nAI的回答：\n")
    get_response(user_question)
