import statistics

# 定义数据列表
data = [5, 10, 15, 20, 25]

# 计算中位数
median = statistics.median(data)

# 计算方差
variance = statistics.variance(data)

# 计算平均数
mean = statistics.mean(data)

# 输出结果
print(f"中位数: {median}")
print(f"方差: {variance}")
print(f"平均数: {mean}")
 