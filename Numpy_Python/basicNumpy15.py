#Random ใช้ array สุ่มค่าตัวเลข
#กำหนดช่วงข้อมูลแต่สุ่มตัวเลข

import numpy as np #เรียกใช้ numpy ในการสร้าง array หรือ มันคือ Numpy array

#2 มิติ , 2 แถว 2 คอลัมน์,2x2
arr =np.random.random((2,2))    
#สร้าง array 2 มิติ ที่สุ่มค่าตัวเลข แบบ float
print(arr)

#3 มิติ , 3 แถว 3 คอลัมน์,3x3
arr2 =np.random.random((3,3)) 
#สร้าง array 3 มิติ ที่สุ่มค่าตัวเลข แบบ float
print(arr2)

#10 มิติ , 10 แถว 10 คอลัมน์,10x10
arr3 =np.random.random((10,10)) 
#สร้าง array 10 มิติ ที่สุ่มค่าตัวเลข แบบ float
print(arr3)