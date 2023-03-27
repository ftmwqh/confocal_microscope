#这个只是为了实验一下
import  numpy as np
from PIL import Image
'''h=Image.open('horizon.jpg')
data=h.getdata()
width,height=h.size
print(data)
data=np.matrix(data,dtype='float')/255
print(data)
new_data=np.reshape(data.getA(),(width,height,3))
print(new_data)
new_data*=255
new_h=Image.fromarray(new_data.astype(np.uint8))
new_h.show()

x=np.array([[100,200,240],[50,80,170],[201,120,111]])

a=Image.fromarray(x)

b=Image.open('horizon.jpg')
data=np.asarray(b)
c=Image.fromarray(data)
print(data)
print(data.shape)

x=np.asarray([[[100,200,240],[50,80,170],[201,120,111]],[[100,200,240],[50,80,170],[201,120,111]],[[100,200,240],[50,80,170],[201,120,111]]])
c=Image.fromarray(x)
pic1=pic.point(lambda x:x>3,'1')#二值化，阈值为3
'''
f=open('a.txt','r')
lines=f.readlines()
m=len(lines)
print('height=',m)
n=len(lines[1].split(' '))
print('width=',n)
I=np.zeros((m,1),dtype=float)

i=0
for line in lines:
    list=line.strip('\n').split(' ')
    print(list)
    I[i]=list[2:n]
    i+=1
I=I.reshape(3,3)
print(I)
print('I0=',I.max())
I_relative=I/I.max()
print('I/I0=',I_relative)
f.close()
pic=Image.fromarray(I_relative*255)
pic=pic.convert('L')
pic1=pic.point(lambda x:x>3,'1')
#pic.show()