import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\desktop\python训练\data.csv")

print(data.info())
print(data.isnull().sum())
print("\n")
print("\"")


for i in data.columns:
    if data[i].dtypes != "object":
        # data[i] = data[i].fillna(data[i].mode().iloc[0])
        # 或者
        # data[i] = data[i].fillna(data[i].mode().values[0])

        # mode() 函数返回类型问题 ：
        # - 代码中使用 data[i].fillna(data[i].mode()) 进行填充，但 data[i].mode() 返回的是一个 pandas Series对象 ，而不是单个数值。
        # - fillna() 函数需要接收一个标量值来填充缺失值，当传入Series时无法正确工作。
        # - 2.
        # 多众数处理问题 ：
        # - 即使数据只有一个众数， mode() 函数也会返回一个包含该值的Series，而不是直接返回标量。
        # - 如果数据存在多个众数（多个值出现的频率相同），返回的Series会包含多个值，这会导致填充失败。
        # - 3.
        # 赋值方式问题 ：
        # - 当将Series赋值给DataFrame的列时，可能会因为索引不匹配导致没有正确填充所有缺失值。
        # data[i] = data[i].fillna(data[i].median())
        data[i] = data[i].fillna(data[i].mean())
        pass
    
print(data.isnull().sum())
print("\n")

columns =data.columns.tolist()

for j in columns:
    # print(data[i].dtypes)
    if data[j].dtypes == "object":
        data = pd.get_dummies(data,columns=[j],drop_first=True)
        
# print(data.info())

new_feature = []

for k in data.columns:
    if k not in columns:
        new_feature.append(k)

# print(new_feature)

for h in new_feature:
    data[h] = data[h].astype(int)
print(data.head())

plt.figure(figsize=(10,6))
# plt.subplot(1,2,1)
sns.boxplot(x=data['Annual Income'])
plt.title('Annual Income')
plt.xlabel('Annual Income')


plt.figure(figsize=(10,6))
# plt.subplot(1,2,2)
sns.histplot(x='Annual Income',hue='Credit Default',data = data,kde = True,element="step")
plt.title('Annual Income')
plt.xlabel('Annual Income')


plt.figure(figsize=(10,6))
# sns.violinplot(x='Credit Default',y='Annual Income',data = data,split=True,hue='Credit Default')
sns.violinplot(x='Credit Default',y='Annual Income',data = data,hue='Credit Default')
# sns.violinplot(x='分类变量', y='数值变量', data=数据框)
plt.title('Annual Income')
plt.xlabel('Annual Income')


plt.figure(figsize=(10,6))
# sns.violinplot(x='Credit Default',y='Annual Income',data = data,split=True,hue='Credit Default')
sns.countplot(x='Number of Open Accounts',data = data,hue='Credit Default')
# sns.violinplot(x='分类变量', y='数值变量', data=数据框)
plt.title('Number of Open Accounts')
plt.xlabel('Number of Open Accounts')
plt.xticks(rotation = 45,ha = "right")
plt.tight_layout()


data["New"] = pd.cut(data['Number of Open Accounts'],bins=[0,5,10,15,20,float('inf')],labels=["0-5","5-10","10-15","15-20","20+"])
plt.figure(figsize=(10,6))
# sns.violinplot(x='Credit Default',y='Annual Income',data = data,split=True,hue='Credit Default')
sns.countplot(x ='New',data = data,hue='Credit Default')
# sns.violinplot(x='分类变量', y='数值变量', data=数据框)
plt.title('Number of Open Accounts')
plt.xlabel('Number of Open Accounts')
plt.xticks(rotation = 45,ha = "right")
plt.tight_layout()

plt.show()
