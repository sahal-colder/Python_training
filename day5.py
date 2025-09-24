# 今天的任务分成以下几步
# 1. 读取数据
# 2. 找到所有离散特征
# 3. 选择一个离散特征进行独热编码
# 4. 采取循环对所有离散特征进行独热编码
# 5. 加上昨天的内容 并且处理所有缺失值

import pandas as pd
data = pd.read_csv('data.csv')

# print(data.info())
print(data.head())

print(data.columns.tolist())
# 可以先看看"Home Ownership"的列名信息，并看其信息的分布数量：
print(data['Home Ownership'].unique())
print(data['Home Ownership'].value_counts())
# print(data[['Home Ownership','Credit Default']].value_counts())
# print(data.value_counts())
print("*************************")

# 寻找所有的离散标签
# columns = data.columns.tolist()
# 列表化
print("*************************")
# print(type(columns))
for feature in data.columns:
    print(type(feature))
    if data[feature].dtype == 'object':
        # print(dis_feature)
        # print(data['Home Ownership'])

        # print(data['Home Ownership'].unique())
        # print(data['Home Ownership'].value_counts())

        data = pd.get_dummies(data,columns=[feature],drop_first=True)# 仅仅针对Home Ownership一行
        # print(data.head)
        # print(data.shape)


# 寻找独热编码后的所有的离散标签
data_origin = pd.read_csv('data.csv')
dis_feature = []
for i in data.columns:
    if i not in data_origin.columns:
        dis_feature.append(i)
# print(dis_feature)
# print(data.head())

# data = pd.get_dummies(data)# 针对 DataFrame 中所有 “分类列”（默认是 object 或 category 类型的列）自动进行独热编码
# print(data.head)
# # print(data.shape)

# data = pd.get_dummies(data,drop_first=True)# 删除独热编码的第一列，（删除冗余信息）
# print(data.head)
# print(data.shape)

# 我感觉直接编码方便一点

# print(dis_feature)
# print(data['Home Ownership'])

# data = pd.get_dummies(data,columns=['Home Ownership'])# 仅仅针对Home Ownership一行
# print(data.head)
# print(data.shape)

# print(data.dtypes)
# 从布尔型转化为整形

for i in dis_feature:
    data[i] = data[i].astype(int)
# print(data.dtypes)
# print(data.isnull().sum())

for j in data.columns:
    if data[j].isnull().sum() != 0:
        data[j] = data[j].fillna(data[j].mean())

print(data.isnull().sum())
