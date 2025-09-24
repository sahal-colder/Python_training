import pandas as pd
data = pd.read_csv("D:\desktop\python训练\data.csv")
# print(data.head())

continuous_features = []
for i in data.columns:
    if i != "objects":
        continuous_features.append(i)
# print(continuous_features)
# print(len(continuous_features))

continuous_features = data.select_dtypes(include = ['float64','int64']).columns.tolist()

# print(continuous_features)
# print(len(continuous_features))


import matplotlib.pyplot as plt
import seaborn as sns

# 设置全局字体为支持中文的字体 (例如 SimHei)
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# plt.figure(figsize=(12,8))
# # plt.subplot(2,1,1)
# # sns.boxplot(x=data["Annual Income"]) # 默认y为数据轴
# sns.boxplot(x='Annual Income',data=data)
# plt.title(' Annual Income')
# plt.xlabel('Annual Income')
# plt.tight_layout()  # 自动调整子图参数，提供足够的空间
# plt.show()

# # # plt.subplot(2,1,2)
# plt.figure(figsize=(12,8))
# # sns.histplot(data['Years in current job'])
# sns.histplot(x='Years in current job',data = data)
# plt.title('在当前工作年限 直方图')
# plt.xlabel('在当前工作年限')
# plt.ylabel('员工数量')
# plt.xticks(rotation=45, ha='right')  # 旋转45度，并右对齐
# plt.tight_layout()  # 自动调整子图参数，提供足够的空间
# plt.show()


# plt.figure(figsize=(8, 6))
# sns.violinplot(x='Credit Default', y='Annual Income',hue='Credit Default', data=data)
# plt.title('Annual Income vs. Credit Default')
# plt.xlabel('Credit Default')
# plt.ylabel('Annual Income')
# plt.show()


# plt.figure(figsize=(12,8))
# sns.histplot(x='Annual Income',hue='Credit Default',data=data,kde=True,element='step')
# # kde=True 是否添加核密度曲线
# # element='step'直方图为何种形状
# # hue为分类指标
# # 纵坐标默认为数据数量
# plt.title('Annual Income vs. Credit Default')
# plt.ylabel('Count')
# plt.xlabel('Annual Income')
# plt.tight_layout() # 自动调整子图参数，提供足够的空间
# plt.show()


plt.figure(figsize=(12,8))
sns.countplot(x='Number of Open Accounts',data = data,hue ='Credit Default')
plt.title('Number of Open Accounts vs. Credit Default')
plt.xlabel('Number of Open Accounts')
plt.ylabel('Count')
plt.xticks(rotation = 45,ha = 'right')
plt.show()


data['Open Accounts Group'] = pd.cut(data['Number of Open Accounts'], bins=[0, 5, 10, 15, 20, float('inf')],
                                      labels=['0-5', '6-10', '11-15', '16-20', '20+']) # 根据你的数据调整分组
#  float('inf')代表正无穷大
plt.figure(figsize=(10, 6))
sns.countplot(x='Open Accounts Group', hue='Credit Default', data=data)
plt.title('Number of Open Accounts (Grouped) vs. Credit Default')
plt.xlabel('Number of Open Accounts Group')
plt.ylabel('Count')
plt.show()

