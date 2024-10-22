import tkinter as tk
from tkinter import messagebox

def convert_temp():
    temp_str = entry.get()
    if temp_str[-1] in ['F', 'f']:
        try:
            celsius = (float(temp_str[:-1]) - 32) / 1.8
            result_label.config(text=f"{celsius:.2f}°C", fg="blue")
        except ValueError:
            messagebox.showerror("输入错误", "请输入正确的温度值")
    elif temp_str[-1] in ['C', 'c']:
        try:
            fahrenheit = 1.8 * float(temp_str[:-1]) + 32
            result_label.config(text=f"{fahrenheit:.2f}℉", fg="red")
        except ValueError:
            messagebox.showerror("输入错误", "请输入正确的温度值")
    else:
        messagebox.showerror("输入格式错误", "温度值必须以F/f或C/c结尾")

# 创建主窗口
root = tk.Tk()
root.title("温度转换器")
root.geometry("400x300")  # 设置窗口大小

# 设置全局字体和颜色
font_style = ("Helvetica", 14)
bg_color = "#f0f0f0"
root.config(bg=bg_color)

# 学号和姓名显示
student_id = "221402060422"  # 替换为你的学号
name = "王仪琳"        # 替换为你的姓名
info_label = tk.Label(root, text=f"姓名: {name}\n学号: {student_id}", font=("Helvetica", 12, "bold"), bg=bg_color)
info_label.pack(pady=10)

# 温度输入框
entry_frame = tk.Frame(root, bg=bg_color)
entry_frame.pack(pady=5)

entry_label = tk.Label(entry_frame, text="请输入带有符号的温度值:", font=font_style, bg=bg_color)
entry_label.pack(side=tk.LEFT)

entry = tk.Entry(entry_frame, font=font_style, width=10)
entry.pack(side=tk.LEFT, padx=10)

# 转换按钮
convert_button = tk.Button(root, text="转换", font=font_style, command=convert_temp, bg="#4CAF50", fg="white", padx=10, pady=5)
convert_button.pack(pady=15)

# 结果显示标签
result_frame = tk.Frame(root, bg=bg_color)
result_frame.pack(pady=20)

result_text_label = tk.Label(result_frame, text="转换后的温度是：", font=font_style, bg=bg_color)
result_text_label.pack(side=tk.LEFT)

result_label = tk.Label(result_frame, text="", font=("Helvetica", 18, "bold"), bg=bg_color)
result_label.pack(side=tk.LEFT)

# 运行主循环
root.mainloop()
