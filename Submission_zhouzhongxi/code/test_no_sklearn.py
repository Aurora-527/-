import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#线性回归算法
train = pd.read_csv("train_.csv")
test = pd.read_csv("test_.csv")
sns.displot(train["outcome"])  
plt.show()
#检测数据的偏度skewness
#print(train["outcome"].skew())

'''
data = train.corr() #将其变成矩阵 
print(data["outcome"].sort_values())
'''

'''查看缺失值
aa = train.isnull().sum()
print(aa)
'''

#删除无关联的属性 
train = train.drop(["id"], axis=1)
test = test.drop(["id"], axis=1)

#汇总train和test的数据
all_data = pd.concat((train, test))
#如果数字，填写均值。如果字符串，填写次数最多的
for col in train.columns:
    if train[col].isnull().sum() > 0:
        if train[col].dtypes == 'object': #字符
            val = all_data[col].dropna().value_counts().idxmax()
            train[col] = train[col].fillna(val)
        else: #数字
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

class LinearRegression:
    def __init__(self):
        self.interception = None #截距b
        self.coef = None #没有w0的w
        self._theta = None #权重向量w
    
    def fit(self,xtrain,ytrain):
        x_b = np.hstack([np.ones((len(xtrain),1)),xtrain]) #第一个特征为1，故须创建一个矩阵与其拼接
        self._theta = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(ytrain) #最小二乘公式
        self.coef = self._theta[1:]
        self.interception = self._theta[0]        
        return self
    
    def predict(self,xtest):
        x_b = np.hstack([np.ones((len(xtest),1)),xtest])
        return x_b.dot(self._theta)

       
lr = LinearRegression()
y = np.log(train["outcome"])#取对数
X = train.drop("outcome",axis=1)
lr = lr.fit(X, y)
results = lr.predict(test)
final = np.exp(results)#返回正常值
   
submission = pd.DataFrame(data={"id": test.index, "outcome": final})
submission.to_csv("submission_a.csv", index= False)
