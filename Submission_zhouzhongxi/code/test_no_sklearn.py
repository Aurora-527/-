import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#线性回归算法

class LinearRegression_SelfDefined():
    def __init__(self):              #1.新建变量
        self.w = None
 
    def fit(self, X, y):              #2.训练集的拟合
        #X = np.insert(X, 0, 1, axis=1)   #增加一个维度
        print (X.shape)        
        X_ = np.linalg.inv(X.T.dot(X))   #公式：求X的转置（.T）与X矩阵相乘（.dot(X)），再求其逆矩阵（np.linalg.inv()）
        self.w = X_.dot(X.T).dot(y)      #上述公式与X的转置进行矩阵相乘，再与y进行矩阵相乘
 
    def predict(self, x):
        y_pred = []
        for element in x:
            y_pred.append(self.__hypothetic(element))
 
        return y_pred

train = pd.read_csv("train_.csv")
test = pd.read_csv("test_.csv")
sns.displot(train["outcome"])  
#plt.show()
#检测数据的偏度skewness
#print(train["outcome"].skew())

"""查看各个指标与目标值的关联程度
y = np.log(train["outcome"])
data = train.corr()
print(data["outcome"].sort_values())
"""

'''查看缺失值
aa = train.isnull().sum()
print(aa[aa>0].sort_values(ascending=False))
'''

#一半是删除过多空值的属性，一半是删除无关联的属性 
train = train.drop(["id"], axis=1)

test = test.drop(["id"], axis=1)

#汇总train和test的数据
all_data = pd.concat((train, test))
#如果数字，填写均值。如果字符串，填写次数最多的
for col in train.columns:
    if train[col].isnull().sum() > 0:
        if train[col].dtypes == 'object':
            val = all_data[col].dropna().value_counts().idxmax()
            train[col] = train[col].fillna(val)
        else:
            val = all_data[col].dropna().mean()
            train[col] = train[col].fillna(val)
for col in test.columns:
     if test[col].isnull().sum() > 0:
         if test[col].dtypes == 'object':
             val = all_data[col].dropna().value_counts().idxmax()
             test[col] = test[col].fillna(val)
         else:
             val = all_data[col].dropna().mean()
             test[col] = test[col].fillna(val)
             
#综合处理，转值类型
for col in all_data.select_dtypes(include = [object]).columns:
      train[col] = train[col].astype('category', categories = all_data[col].dropna().unique())
      test[col] = test[col].astype('category', categories = all_data[col].dropna().unique())

for col in train.columns:
      if train[col].dtype.name == 'category':
         tmp = pd.get_dummies(train[col], prefix = col)
         train = train.join(tmp)
         train = train.drop(col, axis=1)

for col in test.columns:
      if test[col].dtype.name == 'category':
           tmp = pd.get_dummies(test[col], prefix = col)
           test = test.join(tmp)
           test = test.drop(col, axis=1)


        
lr = LinearRegression_SelfDefined()
y = np.log(train["outcome"])
X = train.drop("outcome",axis=1)
lr = lr.fit(X, y)
#！该行代码报错，具体原因待查明  results = lr.predict(test)
final = np.exp(results)
   
   
submission = pd.DataFrame(data={"id": test.index, "outcome": final})
submission.to_csv("submission_b.csv", index= False)
