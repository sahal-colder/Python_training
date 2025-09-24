# 题目:
# 1.创建一个包含三个字符串元素的列表 tech_list，元素分别为 “Python”, “Java”, “Go”。
# 2.获取列表中的第一个元素，并将其存储在变量 first_tech 中。
# 3.向 tech_list 的末尾添加一个新的字符串元素 “JavaScript”。
# 4.修改 tech_list 中的第二个元素（索引为 1），将其从 “Java” 更改为 “Ruby”。
# 5.移除列表中的元素 “Go”。
# 6.计算当前 tech_list 的长度，并将结果存储在变量 current_length 中。
# 7.最后，使用 f-string 分三行打印出以下信息：
    # a.获取到的第一个技术名称。
    # b.列表当前的长度。
    # c.经过所有操作后，列表最终的内容。
    # 打印格式应类似：
    # 第一个技术是: Python
    # 当前列表长度: 3
    # 最终列表内容: [‘Python’, ‘Ruby’, ‘JavaScript’]
    # ————————————————

# tech_list = {"Python","Java","Go"} 集合是无序的
tech_list = ['Python','Java','Go']
print(tech_list)
first_tech = tech_list[0]

# tech_list.append("JavaScript")

# tech_list.extend("JavaScript")
# 添加字符串（会拆分成单个字符）

# insert在索引的前面插入元素
tech_list.insert(len(tech_list),"JavaScript")
print(tech_list)
print(len(tech_list))

tech_list[1] = "Ruby"
tech_list.remove("Go")
# del tech_list[2]  # 删除索引为2的元素（即'Go'）
# print(tech_list)  # 输出: ['Python', 'Java']

# del tech_list[1:3]  # 删除索引1到2的元素（'Java'和'Go'）
# print(tech_list)  # 输出: ['Python', 'JavaScript']
print(tech_list)

current_length = len(tech_list)
print(f"a.获取到的第一个技术名称为：{tech_list[0]}")
print(f"b.列表当前的长度为：{current_length}")
print(f"c.过所有操作后，列表最终的内容为：{tech_list}")


# 循环for语句
# 计算1+100的和 用for循环来写

    # for 变量 in 可迭代对象:
    #     # 循环体（每次遍历执行的代码）
    #     语句1
    #     语句2
    #     ...

total = 0
for i in range(1,101,1):
    # total = total + i
    total += i
print(f"1 + .. + 100 = {total}")
print(i)
# i 没有被释放，python没有循环级作用域


# 温度预警系统
# 1. 定义一个变量temperature存储当前温度（整数）
# 2. 根据以下条件判断并打印预警信息：
#    - 高于35度：打印"红色预警：高温天气！"
#    - 28-35度：打印"黄色预警：天气炎热"
#    - 20-27度：打印"绿色提示：适宜温度"
#    - 低于20度：打印"蓝色预警：注意保暖"
# 3. 使用if-elif-else结构实现
# 4. 测试用例：用38你的代码
# ————————————————

# if 条件1:
#     # 条件1为 True 时执行
#     语句块1
# elif 条件2:
#     # 条件1为 False，且条件2为 True 时执行
#     语句块2
# elif 条件3:
#     # 前面条件都为 False，且条件3为 True 时执行
#     语句块3
# ...
# else:
#     # 所有条件都为 False 时执行（可选）
#     语句块N

temperature = 10
if temperature > 35 :
    print("红色预警：高温天气！")
elif temperature >= 28 and temperature <= 35:
    print("黄色预警：天气炎热")
elif temperature >= 20 and temperature < 28:
    print("绿色提示：适宜温度")
else :
    print("蓝色预警：注意保暖")


# 定义一个包含整数的列表 scores，赋值为 [85, 92, 78, 65, 95, 88]。
# 初始化两个变量：excellent_count 用于记录分数大于等于 90 的个数，初始值为 0；total_score 用于累加所有分数，初始值为 0。
# 使用 for 循环遍历 scores 列表中的每一个分数。
# 在循环内部：
# 将当前分数累加到 total_score 变量上。
# 使用 if 语句判断当前分数是否大于等于 90。如果是，则将 excellent_count 变量加 1。
# 循环结束后，计算平均分 average_score（总分除以分数的个数）。
# 使用 f-string 分三行打印出以下信息：
# 优秀分数（>=90）的个数。
# 所有分数的总和。
# 所有分数的平均分（结果包含3位小数）。
# ————————————————

scores = [85,92,78,65,95,88]
excellent_count = 0; total_score = 0
average_score = 0

for i in range(len(scores)):
    total_score = total_score + scores[i]
    if scores[i] >= 90:
        excellent_count += 1
    pass

average_score = total_score/len(scores)

print(f"优秀分数>=90的个数:{excellent_count}")
print(f"所有分数的总和:{total_score}")
print(f"所有分数的平均分:{average_score:.3f}")