import re

# 1. 搜索匹配的字符串
pattern = r'\d+'  # 匹配数字
text = '我有 2 个苹果和 3 个橙子。'
result = re.findall(pattern, text)
print(result)  # 输出: ['2', '3']

# 2. 替换
text = '电话: 123-456-7890'
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(new_text)  # 输出: 电话: XXX-XXX-XXXX

# 3. 验证邮箱
email = 'test@example.com'
if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print("有效的邮箱")
else:
    print("无效的邮箱")

# 4. 匹配时间
text = "现在时间是 14:30，会议开始时间是 09:00。"
times = re.findall(r'(?:[01]\d|2[0-3]):[0-5]\d', text)
print(times)

#  5
s = '''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jack'><span id='3'>大聪明</span></div>
<div class='lili'><span id='4'>范思哲</span></div>
<div class='tony'><span id='5'>胡说八道</span></div>
'''

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S)

result = obj.finditer(s)

for it in result:
    print(it.group("wahaha"))
    print(it.group("id"))

