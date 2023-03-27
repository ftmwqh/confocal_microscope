#这个是绘制二维图的
import  numpy as np
from PIL import Image

f=open(输入文件名,'r')
lines=f.readlines()
m=len(lines)
print('height=',m)
n=len(lines[1].split(' '))
print('width=',n)
I=np.zeros((m,1),dtype=float)

i=0
for line in lines:
    list=line.strip('\n').split(' ')
    I[i]=list[0:n]
    i+=1
    #把文件读入到一个矩阵
print('I0=',I.max())
I_relative=I/I.max()#归一化
I_relative=I_relative.reshape(输入矩阵行数,输入矩阵列数)#把一行的转变成真正的原矩阵形式
print('I/I0=',I_relative)

pic=Image.fromarray(I_relative*255)#带入画图
pic=pic.convert('L')
pic.show()
