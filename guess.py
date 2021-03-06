# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大/小
# 一邊猜一邊印出猜了第幾次
# 讓使用者決定隨機數字的範圍

import random
s = input('請決定隨機範圍始於: ')
e = input('請決定隨機範圍終於: ')
s = int(s)
e = int(e)
r = random.randint(s, e)               # 有包含1和100
i = 0                                    # 要放在while True的外面，因為如果放在裡面，每猜一次，計次會歸零
while True:                              # while要記得小寫
    i += 1   #i = i + 1                              
    num = input('請輸入數字: ')  # 要放在while True底下!放在上面的話回圈會跑不到，不會重複詢問
    num = int(num)                        
    if num == r:                         # 記得，要一樣(即等於)時，要用==
        print('終於猜對了!')
        print('這是你猜的第', i, '次')     #這邊要寫，不然break的時候第22行不會執行到
        break
    elif num > r:
        print('要再小一點唷~')
    elif num < r:
        print('要再大一點唷~')
    print('這是你猜的第', i, '次')         #寫在最下面才不需要寫三次(程式重複性越低越好)