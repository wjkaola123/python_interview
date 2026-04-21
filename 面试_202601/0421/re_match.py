import re

text = "abc123xyz456ppp"

print(re.match(r'\d+', text))
s = re.search(r'\d+', text)
print(s.group())
s = re.findall(r'\d+', text)
print(s)

s = re.search(r'(\d{3})-(\d{4})', "订单号: 123-4567")
print(s.group())  # 输出: 123-4567
print(s.group(0))  # 输出: 123-4567（等价）

print(s.group(1))  # 输出: 123（第一个括号捕获的内容）
print(s.group(2))  # 输出: 4567（第二个括号捕获的内容）
print(s.groups())  # 输出: ('123', '4567')

# 提取日期中的年、月、日
date_str = "今天是 2024-05-20"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)

if match:
    year = match.group(1)  # 2024
    month = match.group(2)  # 05
    day = match.group(3)  # 20
    print(f"年: {year}, 月: {month}, 日: {day}")

    # 或者一次性获取所有部分
    print(match.groups())  # ('2024', '05', '20')
