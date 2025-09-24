# 题目1: 定义两个字符串变量，str1 赋值为 “Hello”，str2 赋值为 “Python”。
# 将这两个字符串拼接起来（中间加一个空格），并将结果存储在变量 greeting 中；
# 计算 greeting 字符串的长度，存储在变量 length 中；
# 获取 greeting 字符串的第一个字符，存储在变量 first_char 中。然后，使用 f-string 分三行打印出类似以下格式的信息：
# 拼接结果: Hello Python
# 字符串长度: 12
# 第一个字符: H
# 第二个字符：e
# 最后一个字符是：n
# ————————————————
str1 ="Hello";str2 = "Python"
greeting = str1 + " " + str2
# print(greeting)
length = len(greeting)
first_char = greeting[0]
print(f"拼接结果: {greeting}\n字符串长度:{length}\n第一个字符: {first_char}\n第二个字符：{greeting[1]}\n最后一个字符是：{greeting[-1]}")
print("____________\n")

# 定义两个整数变量，score_a 赋值为 75，score_b 赋值为 90。比较 score_a 是否大于 score_b，将比较结果（布尔值）存储在变量 is_a_higher 中；
# 比较 score_a 是否小于等于 score_b，将结果存储在变量 is_a_lower_or_equal 中；
# 比较 score_a 是否不等于 score_b，将结果存储在变量 is_different 中。然后，使用 f-string 分三行打印出类似以下格式的信息：
# 75 是否大于 90: False
# 75 是否小于等于 90: True
# 75 是否不等于 90: True
# ————————————————
score_a = 75
score_b = 90

is_a_higher = score_a>score_b
is_a_lower_or_equal = score_a<=score_b
is_different = score_a != score_b

print(f"{score_a} 是否小于等于 {score_b}:{is_a_lower_or_equal}\n{score_a} 是否大于 {score_b}:{is_a_higher}")
print(f"{score_a} 是否不等于 {score_b}:{is_different}")


