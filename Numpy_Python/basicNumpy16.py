#NumPy Attribute  คือส่วนที่บอกโครงสร้าง ของ array ที่เราสร้างมา ว่ามีลักษณะอะไรบ้าง โดยใช้คำสั่ง array_name.attribute

import numpy as np #เรียกใช้ numpy 

#เราจะสร้าง array มา 2 ก้อน เป็น array 1 มิติ กับ array 2 มิติ

arr1d=np.array([1,2,3,4,5])#สร้าง array 1 มิติ
print(arr1d)

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])#สร้าง array 2 มิติ

#อยากรู้ว่า array นั้นเป็น array 1 มิติหรือ array 2 มิติ
print(arr1d.ndim,"mit")
print(arr2d.ndim,"mit")

#อยากเช็คชนิดข้อมูลของ array นั้น
print(arr1d.dtype,"ของ array 1 มิติ")
print(arr2d.dtype,"ของ array 2 มิติ")

#หรือกำหนด dtypeให้ arr2d
#แบบ float
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="float")
print(arr2d)#แสดงข้อมูลใน array
print(arr2d.dtype)#เช็คชนิดข้อมูล

#แบบ complex
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="complex")
print(arr2d)#แสดงข้อมูลใน array
print(arr2d.dtype)#เช็คชนิดข้อมูล

#แบบ int
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="int")
print(arr2d)#แสดงข้อมูลใน array
print(arr2d.dtype)#เช็คชนิดข้อมูล
#ไม่จำเป็นต้องใส่ dtype ก็ได้แบบ int เพราะมันเป็นแบบ int อยู่แล้ว จะแสดงตัวอย่างให้ดูว่าเป็น int อยู่แล้วจริงไหม
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b.dtype)

#แบบ object
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="object")
print(arr2d)#แสดงข้อมูลใน array
print(arr2d.dtype)#เช็คชนิดข้อมูล

#อยากรู้ รูปร่างของ array นั้น โดยใช้คำสั่ง .shape
print(arr1d.shape)

#หรือให้เห็นภาพชัดๆ
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c.shape)

d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d.shape)

#อยากรู้ขนาดของ array นั้น โดยใช้คำสั่ง .size ว่าแบบ array เก็บไว้เท่าไหร่
e=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(e.size)
f=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(f.size)

#itemsize ว่าแบบ array จะเป็นตัวที่บอกขนาดของ array นั้นโดยอ้างอิงกับชนิดข้อมูลที่กำหนดใน arrray ตัวนั้น
g=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(g.dtype)#ดูก่อนสิว่า ชนิดข้อมูลของ array อะไรหน้อ
print(g.itemsize) #อยากรู้ว่า กี่ byte ,1 byte = 8 bit เช่น int เป็น 4 byte เพราะมันเป็น 32 bit เอามาหารด้วย 8 จะได้ 4
#มาดู itemsize ของ complex กับ float กับ int กับ object กับ str กับ unicode

h=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="complex")
print(h.dtype)
print(h.itemsize)

i=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="float")
print(i.dtype)
print(i.itemsize)

j=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="int")
print(j.dtype)
print(j.itemsize)

k=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="object")
print(k.dtype)
print(k.itemsize)

l=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="str")
print(l.dtype)
print(l.itemsize)

m=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype="unicode")
print(m.dtype)
print(m.itemsize)
