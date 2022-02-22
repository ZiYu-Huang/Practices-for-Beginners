#讓使用者重複地輸入商品名稱(購買過的東西)及商品價格
#因為要重複輸入，所以用while loop比較合適(不知道會執行多少次用)，比起for loop(固定次數執行)
#因為要對應名稱和價格，所以是二維清單
#二維清單即大火車內有各個小小清單組成
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ') #寫第一個break下面，才不用前面商品不輸入了還再問一次
    #p = [] 小清單        # 較直覺的寫法:先建立小清單p
    #p.append(name)       # 再把兩個屬性加到p中
    #p.append(price)
    #products.append(p)   #最後把小清單p加到大清單products中 #小清單都放到大清單裡面，完成2維清單
    products.append([name, price]) #上面四行簡潔成一行就可以了 #記得裡面要放中括號 #兩個屬性直接建立小清單，放到大清單products中

print(products)               # [['ramen', '100'], ['pasta', '200']]

#清單的索引標籤叫做index
print(products[0][0])    # 先找出大清單中的第0格，再找到小清單中的第0格 #ramen

# Q: 寫出每個商品對應的價格
for p in products:
    print(p[0], '的商品價格為: ', p[1])
    print(p)     #是把每一個小清單拿出來
    print(p[0])  #是把每一個小清單中的第0格拿出來