<div align = "center">数智一轮考核学习成果</div>

​																												by： aurora

# 一.线性回归

## 1.定义：

​			   线性：指可加性和齐次性

​			   回归：确定多个变量间相互依赖的定量关系

## 2.实质：

找到一条线/超平面来拟合这些样本点，使他们之间的误差尽可能的小。而不同的线/超平面（不同的参数值）对应着不同的误差，我们需要找到让误差最小的线/超平面。



## 3.损失函数：

回归任务常用的损失函数有三种：均方误差（MSE）、均方根误差（RMSE）、平均绝对误差（MAE）,公式依次如下：

![image-20220325215924080](C:\Users\AURORA\AppData\Roaming\Typora\typora-user-images\image-20220325215924080.png)

![image-20220325220005584](C:\Users\AURORA\AppData\Roaming\Typora\typora-user-images\image-20220325220005584.png)

![image-20220325220012749](C:\Users\AURORA\AppData\Roaming\Typora\typora-user-images\image-20220325220012749.png)

## 4.最小化误差两法

### 最小二乘法：

![image-20220325220424748](C:\Users\AURORA\AppData\Roaming\Typora\typora-user-images\image-20220325220424748.png)



### 梯度下降法：

![img](https://img-blog.csdnimg.cn/20201101095525256.png#pic_center)

![img](https://img-blog.csdnimg.cn/20201101111133605.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDY5NzE5OA==,size_16,color_FFFFFF,t_70#pic_center)

理解：这里再举个生活中的栗子，梯度下降法中随机给a赋一个预设值就好比你随机出现在一个山坡上，然后这时候你想以最快的方式走到山谷的最低点，那么你就得判断你的下一步该往那边走，走完一步之后同样再次判断下一步的方向，以此类推就能走到山谷的最低点了。而公式中的α我们称它为学习率，在栗子中可以理解为你每一步跨出去的步伐有多大，α越大，步伐就越大。（实际中α的取值不能太大也不能太小，太大会造成损失函数J接近最小值时，下一步就越过去了。好比在你接近山谷的最低点时，你步伐太大一步跨过去了，下一步往回走的时候又是如此跨过去，永远到达不了最低点；α太小又会造成移动速度太慢，因为我们当然希望在能确保走到最低点的前提下越快越好。）
[摘自csdn]



# 二、数据预处理

## 1.缺失值处理：

如果某个属性空值过多（超过15%时），直接从数据中删除该属性。

如果空值占比不大，如果是数字类型，就填写均值。如果是字符串类型，就填写出现次数最多的字符串。