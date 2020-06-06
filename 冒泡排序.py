import numpy as np 
x=np.random.randint(1,100,20)
# 随机生成20个数
print("排序前",x)
for j in range(len(x)-1):
    for i in range(len(x)-1):
        if(x[i]>x[i+1]):
            t=x[i+1]
            x[i+1]=x[i]
            x[i]=t
print("排序后",x)
