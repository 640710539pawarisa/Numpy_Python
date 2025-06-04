#Arange 
#การสร้าง array 1 มิติแบบกำหนดช่วง โดยโครงสร้าง arange จะคล้ายๆกับ range ที่อยู่ใน list 
#เช่น arange(1,10) = [1,2,3,4,5,6,7,8,9] มันคือ np.arange(start,stop,step,dtype)
# หรือ#np.arange(start,stop,step) หรือ np.arange(stop) หรือ np.arange(stop,dtype)
#หรือ np.arange(start,stop,dtype)
#*********

import numpy as np #เรียกใช้ numpy ในการสร้าง array หรือ มันคือ Numpy array

arr =np.arange(10)#สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง 0 ถึง 10
print(arr)

arr2=np.arange(10.0)#สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง 0.0 ถึง 10.0
print(arr2)

#หรือระบุช่วงตัวเลข
#np.arange(start,stop,step)
a=np.arange(1,10) #สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง 1 ถึง 10
print(a)

a2 = np.arange(3,4)
print(a2)

#หรือทำแบบติดลบ
a3 =np.arange(-3,3) #สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง -3 ถึง 3
print(a3)

a4 = np.arange(-1,10) #สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง -1 ถึง 10
print(a4)

#หรือแบบนี้ก็ได้
#np.arange(start,stop,step,dtype)
b = np.arange(1,10,1,dtype = "int") #สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง 1 ถึง 10 เพิ่มขึ้นเป็น 1
print(b)

c =np.arange(1,20,2,dtype = "int") #สร้าง array 1 มิติ ที่สามารถระบุช่วงตัวเลขได้ , =ช่วง 1 ถึง 20 เพิ่มขึ้นเป็น 2
print(c)

#แบบ float
d=np.arange(1,20,2,dtype = "float")
print(d)

#แบบ complex
e=np.arange(1,20,2,dtype = "complex")
print(e)

#แบบ object
f=np.arange(1,20,2,dtype = "object")
print(f)

#แบบไม่กำหนดstepแต่กำหนด start และ stop และ dtype
g=np.arange(1,20,dtype = "int")
print(g)