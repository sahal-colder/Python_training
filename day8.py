import pandas as pd
data = pd.read_csv(r"D:\desktop\python训练\data.csv")

# print(data.head())
# print(data['Home Ownership'].value_counts())

# mapping = {"Home Mortgage":0,"Rent":1,"Own Home":2,"Have Mortgage":3}
# data['Home Ownership'] = data['Home Ownership'].map(mapping)

# print(data["Home Ownership"].head())
# print(data['Home Ownership'].value_counts())

# #######################################################################

# mapping = {"Short Term":0,"Long Term":1}
# data['Term'] = data['Term'].map(mapping)

# print(data["Term"].head())
# print(data['Term'].value_counts())

# ######################################################################

# 嵌套字典
mapping = {
    "Term": {
        "Short Term": 1,
        "Long Term": 0
    },
    "Home Ownership": {
        "Rent": 0,
        "Own Home": 1,
        "Have Mortgage  ": 2,
        "Home Mortgage": 3
    }
}
 
# mapping = {"Short Term":0,"Long Term":1}
data["Term"] = data["Term"].map(mapping["Term"])

# print(data["Term"].head())
# print(data['Term'].value_counts())

# def manual_normalize(data):
#     data_min = data.min()
#     data_max = data.max()

#     normalized_data = (data - data_min)/(data - data_max)

#     return normalized_data

# data["Annual Income"] = manual_normalize(data["Annual Income"])
# print(data["Annual Income"].head())


from sklearn.preprocessing import StandardScaler

scarler = StandardScaler()

data["Annual Income"] = scarler.fit_transform(data[["Annual Income"]])
print(data["Annual Income"])
print(data[["Annual Income"]])