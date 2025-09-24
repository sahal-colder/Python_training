# 定义三个变量 a, b, c，并分别将整数 1, 2, 3 赋值给它们。
# 然后，使用 print() 函数将每个变量的值单独打印出来，每个值占一行。
a=1;b=2;c=3
print (a,b,c)
print("a =",a,"\nb =",b,"\nc =",c)

# 创建两个变量：name 存储你的名字（字符串，例如 "小明"）
# city 存储你所在的城市（字符串，例如 "北京"）。使用 f-string 将这两个变量组合成一句话并打印出来。
name="小明";city="北京"
print(f'你的名字是：{name}')
print(f'你的城市是：{city}')
print(f"你的名字是：{name},你的城市是：{city}。")

# 定义两个整数变量，num1 赋值为 20，num2 赋值为 8。计算这两个变量的和，并将结果存储在一个新的变量 a 中；
# 计算这两个变量的商，叫做b；计算这两个变量的余数，叫做c。然后，使用 f-string 打印出类似 “20 加 8 的结果是：28” 的信息，分成三行打印。
num1=20;num2=8
a=num1+num2
b=num1/num2
c=num1%num2
print(f"20+8={a}\n20/8={b}\n20%8={c}")

# 题目4: 定义两个浮点数变量，price 赋值为 19.9，discount 赋值为 0.8 (表示 8 折)。
# 计算折扣后的价格，并将结果存储在变量 final_price 中；计算节省了多少钱，存储在变量 saved_amount 中。
price=19.9
discount=0.8
final_price=price*discount
saved_amount=price-final_price
print(f"计算折扣后的价格:{final_price}\n计算节省了{saved_amount}钱")
print(f"计算折扣后的价格:{final_price}\n计算节省了{saved_amount:.2f}钱")# f小数
print(f"计算折扣后的价格:{final_price}\n计算节省了{saved_amount:.2g}钱")# g有效数字

print("\"")