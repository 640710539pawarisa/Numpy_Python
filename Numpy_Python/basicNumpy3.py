#สร้าง array 3 มิติ ,ต้องเก็บใส่ใน bracket []  
#array จะindex เริ่มต้นเป็น 0 
#จะรู้ได้ไงว่าเป็นกี่มิติ ให้ดูที่ bracket [[],[]] หรือ [[],[],[]] ก็เป็น array 2 มิติ
# แต่ถ้า 3 มิติ ให้ดูที่ bracket [[],[],[]] ก็เป็น array 3 มิติ

#เรียกใช้ numpy ในการสร้าง array หรือ มันคือ Numpy array
import numpy as np #ตั้งชื่อ numpy เป็น np

arr1D =np.array([1,2,3,4,5]) #สร้าง array 1 มิติ
print(arr1D ,"Array 1 มิติ")

arr2D =np.array([[1,2,3],[4,5,6]]) #สร้าง array 2 มิติ
print(arr2D ,"Array 2 มิติ")

#เช็คว่า array นั้นเป็น array 2 มิติหรือไม่
print(arr2D.ndim,"mit")

#สร้าง array 3 มิติ
arr3D = np.array([[[1,2,3],[4,5,6]]]) #สร้าง array 3 มิติ
print(arr3D)

#เช็คว่า array นั้นเป็น array 3 มิติหรือไม่
print(arr3D.ndim,"mit")

#ทำแบบ list ก็ได้
li = [[[1,2,3],[4,5,6]]] #เก็บไว้ในตัวแปรชื่อ li ก่อนก็ได้ แล้วค่อยนําไปสร้าง array
b = np.array(li) #สร้าง array 3 มิติ
print(b)

#ทำแบบ tuple ก็ได้
tu = (((1,2,3),(4,5,6))) #เก็บไว้ในตัวแปรชื่อ tu ก่อนก็ได้ แล้วค่อยนําไปสร้าง array
c = np.array(tu) #สร้าง array 3 มิติ
print(c)

