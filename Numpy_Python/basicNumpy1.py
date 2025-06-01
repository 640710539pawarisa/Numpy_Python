#การสร้าง array
# Array 1 มิติ มันจะนำสมาชิกมาเรียงต่อกันเป้นแถว ******

#เรียกใช้ numpy ในการสร้าง array หรือ มันคือ Numpy array
import numpy as np #ตั้งชื่อ numpy เป็น np

#สร้าง array 0 มิติ
array0D = np.array(1)
print(array0D)

array0D = np.array(2)
print(array0D)

#เช็คว่า array นั้นเป็น array 0 มิติหรือไม่
print(array0D.ndim,"mit")
#----------------------------------------------------------
#สร้าง array 1 มิติ เก็บไว้ในตัวแปรชื่อ array1D  ,ต้องเก็บใส่ใน bracket []
array1D =  np.array([1,2,3,4,5])
print(array1D)

#เช็คว่า array นั้นเป็น array 1 มิติหรือไม่
print(array1D.ndim,"mit")

#สร้างเก็บเป็นlist ก็ได้
li = [1,2,3,4,5] #เก็บไว้ในตัวแปรชื่อ li ก่อนก็ได้ แล้วค่อยนําไปสร้าง array
b = np.array(li)
print(b)

#สร้างเก็บเป็นtuple ก็ได้ tuple = (...,...,....,...)
tu = (1,2,3,4,5) #เก็บไว้ในตัวแปรชื่อ tu ก่อนก็ได้ แล้วค่อยนําไปสร้าง array
c = np.array(tu)
print(c)

#หรือเขียนแบบนี้ก็ได้ คือแบบ tuple
d=np.array((1,2,3,4,5))
print(d)