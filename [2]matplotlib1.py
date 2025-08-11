import numpy as np
import matplotlib.pyplot as plt

# y = [5,20,10,15,10]
# x = ['Mon','Tue','Wed','Thu','Fri']
# plt.plot(x,y) # คำสั่งสร้างกราฟ
# plt.show() # สั่งแสดงกราฟ


# ==============================================
#               การปรับขนาดกราฟ
# ==============================================

# y = np.random.randint(1,11,5) # สร้าง array ที่มีตัวเลขตั้งแต่ 1 - 10 จำนวน 5 ตัว
# x = list('ABCDE') # แปลง String ให้กลายเป็น array list ['A','B','C','D','E']

# plt.rcParams['figure.figsize'] = (10,5) #width = 10" , height = 5"

# # หรืออีกแบบคือ
# # plt.figure(figsize=(10,5))

# plt.plot(x,y)
# plt.show()

# ========== Function style.use()

# plt.style.use('seaborn-v0_8')
# y = np.random.randint(1,11,5) # สร้าง array ที่มีตัวเลขตั้งแต่ 1 - 10 จำนวน 5 ตัว
# x = list('ABCDE') # แปลง String ให้กลายเป็น array list ['A','B','C','D','E']

# # print(plt.style.available) เพื่อเช็ครายชื่อ style

# plt.plot(x,y)
# plt.show()



