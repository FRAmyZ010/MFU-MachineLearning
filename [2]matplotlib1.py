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




# ======== การใส่ข้อความต่างๆ

# plt.style.use('seaborn-v0_8')

# y=[15,12,19,13,16,17,12]
# x=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

# plt.title('Weekly Sales', color = 'blue', alpha=0.8)
# plt.ylabel('Amount', color='m',fontsize=14)
# plt.xlabel('Weekday',c='g',fontsize=14)
# plt.yticks(c='r')
# plt.xticks(rotation='vertical',c='r',fontsize=13)
# plt.plot(x, y)
# plt.show()


# ================= LEGEND

x = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
y = [120,100,150,200,300,100,140]

plt.plot(x,y,ls=':',c='r',label='G1')

y = [80,100,110,105,240,200,170]
plt.plot(x,y,ls='--',c='b',label='G2')

plt.legend(loc='best')
plt.show()