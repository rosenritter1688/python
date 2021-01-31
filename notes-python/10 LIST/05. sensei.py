Listx = [ [1,2,'A'], [['A','B',100],200], 300]
print(Listx)
#*[[1, 2, 'A'], [['A', 'B', 100], 200], 300]


Listx.append('400');print(Listx)
#*[[1, 2, 'A'], [['A', 'B', 100], 200], 300, '400']
Listx.append(['x','y','z']);print(Listx) #掛上一項在最後, ['x','y','z'] 為一項, 掛在最後
#*[[1, 2, 'A'], [['A', 'B', 100], 200], 300, '400', ['x', 'y', 'z']]
Listx.extend(['x1','y1','z1']); print(Listx) #插入多項, ['x1','y1','z1']變 3 項
#*[[1, 2, 'A'], [['A', 'B', 100], 200], 300, '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1']
Listx[0] = "Updated";   print(Listx) #更改單項的內容
#*['Updated', [['A', 'B', 100], 200], 300, '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1']
Listx.insert(0,"Inserted");print(Listx) #插入一項在第0項之(前)
#*['Inserted', 'Updated', [['A', 'B', 100], 200], 300, '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1']
Listx.remove(300); print(Listx) #刪除value = 300的項目
#*['Inserted', 'Updated', [['A', 'B', 100], 200], '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1'] 
del Listx[0]; print(Listx) #刪除第0項
#*['Updated', [['A', 'B', 100], 200], '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1']
print(Listx + [999, 888]) #兩 list 前後串, 與 extend一樣
#*['Updated', [['A', 'B', 100], 200], '400', ['x', 'y', 'z'], 'x1', 'y1', 'z1', 999, 888] 
print([1,2,3] * 2) # list 再重複一遍
#*[1, 2, 3, 1, 2, 3]
print("[0,1,2,3,4,5,6][1:4]=>", [0,1,2,3,4,5,6][1:4]) # list 取第1項到第(4-1)項
#*[0,1,2,3,4,5,6][1:4]=> [1, 2, 3]

print(8 in [1,2,3]) #False
#*False
Listx = list('Hello'); print(Listx) #字串轉為清單
#*['H', 'e', 'l', 'l', 'o']





    

      


