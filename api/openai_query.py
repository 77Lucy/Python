import openai
import os

# 设置您的OpenAI API密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个有帮助的助手。"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"发生错误：{str(e)}"

def main():
    while True:
        user_input = input("请输入您的问题（输入'退出'结束程序）：")
        if user_input.lower() == '退出':
            print("谢谢使用，再见！")
            break
        
        answer = query_openai(user_input)
        print("\nAI的回答：")
        print(answer)
        print("\n")

if __name__ == "__main__":
    main()
