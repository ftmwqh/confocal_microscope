#画三维图
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def con(name,height,threshold):#文件名、登高面高度、光强判断阈值
    f=open(name,'r')
    lines=f.readlines()
    m=len(lines)
    n=len(lines[1].split(' '))
    I=np.zeros((m,1),dtype=float)
    i=0
    for line in lines:
        list=line.strip('\n').split(' ')
        I[i]=list[0:n]
        if I[i]<0:
            I[i]=0
        i+=1
    print('I0=',I.max())
    I_relative=I/I.max()
    I_relative=I_relative.reshape(12,12)
    print('I/I0=',I_relative)
    x=np.linspace(0,5.5,12)
    y=np.linspace(0,5.5,12)
    x,y=np.meshgrid(x,y)
    z=np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            if I_relative[i][j]>threshold:#光强达到阈值则认为处于等高面上
                z[i][j]=height
    return z
z1=con('bottom.txt',0,0.5)
z2=con('mid_bottom.txt',1,0.5)
z3=con('mid.txt',1.5,0.5)
z4=con('mid_top.txt',2,0.5)
z5=con('top.txt',2.5,0.5)#5个文件的数据
x=np.linspace(0,5.5,12)
y=np.linspace(0,5.5,12)
x,y=np.meshgrid(x,y)
z=np.zeros((len(x),len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        z[i][j]=max(z1[i][j],z2[i][j],z3[i][j],z4[i][j],z5[i][j])
        #我没想到太好的方法，就把五个文件得到的数据在同一点取最高的那个
        '''if z5[i][j]==1.0:
            z[i][j]=z5[i][j]'''#这里是如果想要把最上面那个奇怪的点变成钉子内部凹槽写的，看您做出决定
fig=plt.figure()
ax=fig.add_subplot(projection='3d')
ax.plot_surface(x,y,z)
plt.show()
