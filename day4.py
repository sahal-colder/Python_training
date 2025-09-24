# 首先导入pandas库并读取数据：
import pandas as pd
data = pd.read_csv('data.csv')

print(data.isnull()) 
# 布尔矩阵显示缺失值，这个方法返回一个布尔矩阵，也是dataframe对象，
# 其中True表示对应位置的值是缺失值，False表示对应位置的值不是缺失值。

print(data['Annual Income'].isnull().sum())
# 计算特定列缺失值个数 吗，默认axis = 0

print('*********************')
print(data.isnull().sum(axis=0)) 
print('*********************')
# 计算每列缺失值个数 吗，默认axis = 0

print(data.head(10))
# 默认前五行

print(data.info()) 
# data.info() “打开说明书并展示内容”（执行这个功能，输出表格的元信息）。

print(data.shape)
print(data.columns)

# 在 Pandas 中，describe() 是 DataFrame 或 Series 对象的方法，
# 用于快速生成描述性统计摘要，帮助你理解数据的分布特征。
print(data.describe())

print(data.dtypes)
print(data.count())

# 补全数据
print(data['Annual Income'].median())
# 单列多列均可，此数据列表中存在文字数据


# data['Annual Income'].fillna(data['Annual Income'].median(),inplace = True)
# pandas觉得这样不安全
# data['Annual Income'] 可能只是原始数据的一个 “临时副本”（不是直接操作原始数据本身）。这时候用 inplace=True 去 “原地修改”
# 可能改不到真正的原始数据（相当于你想在原书上改字，结果改在了复印件上）。
# Pandas 3.0 以后会彻底禁止这种写法，所以提前警告你。

data['Annual Income'] = data['Annual Income'].fillna(data['Annual Income'].median())
print(data['Annual Income'].isnull().sum())

print((data['Annual Income'].median()))
# print(data['Home Ownership'].)

######################################################################################################################
# 用众数填充
import pandas as pd
data = pd.read_csv('data.csv')
print(data['Annual Income'].isnull().sum())

mode = data['Annual Income'].mode()
print(mode)
print(data['Annual Income'].isnull().sum())

# mode为众数
data['Annual Income'] = data['Annual Income'].fillna(mode[0])
print(data['Annual Income'].isnull().sum())

# mode = data['Annual Income'].mode()
# print(mode)

# tolist() 是 将数组 / 序列类型数据转换为 Python 原生列表（list） 的方法
c = data.columns.tolist() 
# print(type(c))
# print(c)
print('********************************')

for i in c:
    if data.dtypes[i] != 'object' :
        if data[i].isnull().sum() != 0:
            mean = data[i].mean()
            data[i] = data[i].fillna(mean)

# for i in data.columns.tolist():
#     if data.dtypes[i] != 'object' :
#         if data[i].isnull().sum() != 0:
#             mean = data[i].mean()
#             data[i] = data[i].fillna(mean)

print(data.isnull().sum())