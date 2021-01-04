import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
import sqlite3



win = Tk()
win.geometry('800x1000')


x= ['貢寮淨水場', '平溪淨水場', '坪林淨水場', '石門淨水場', '大湳淨水場', '龍潭淨水場', '大湖淨水場', '大湖二場淨水場', '明德淨水場', '三水源淨水場', '公館淨水場', '四水源淨水場', '阿丹淨水場', '二崙淨水場', '西螺淨水場', '莿桐淨水場', '土庫淨水場', '平和淨水場', '南化淨水場', '潭頂淨水場', '楠玉淨水場', '鏡面淨水場', '內埔農工淨水場', '長治百合淨水場', '屏東農場淨水場', '禮納里淨水場', '澄清湖淨水場', '路竹淨水場', '嶺口淨水場', '小坪淨水場', '丸山淨水場', '東澳淨水場', '金洋淨水場', '柑仔坑淨水場', '寒溪淨水場', '碧候淨水場', '廣興淨水場', '澳花淨水場', '蘇澳淨水場', '大溪淨水場', '四季淨水場', '圳頭淨水場', '枕山淨水場', '松羅淨水場', '金面淨水場', '英士淨水場', '深溝淨水場', '龍潭淨水場', '清洲淨水場', '利嘉淨水場', '初鹿淨水場', '泰安淨水場', '黑森林淨水場', '土板淨水場', '大王淨水場', '加羅板淨水場', '正興淨水場', '安朔淨水場', '金崙淨水場', '愛國埔淨水場', '嘉蘭淨水場', '水母淨水場', '成功淨水場', '紅葉淨水場', '瑞豐淨水場', '關山淨水場']
b=[6.99, 7.54, 7.55, 7.97, 7.18, 7.95, 7.57, 7.47, 7.78, 7.2, 8.01, 7.02, 7.52, 7.81, 6.93, 8.07, 7.3, 7.48, 8.26, 8.27, 8.01, 7.88, 7.27, 7.86, 6.94, 6.41, 6.74, 7.25, 7.43, 7.69, 6.43, 7.23, 8.21, 7.6, 7.76, 7.67, 6.63, 7.68, 6.39, 7.75, 7.75, 7.35, 7.72, 7.26, 7.6, 7.01, 7.12, 7.31, 7.37, 8.33, 7.03, 8.19, 8.34, 7.56, 6.9, 7.48, 6.83, 7.08, 8.12, 7.7, 7.84, 7.68, 7.78, 8.28, 7.08, 7.91]
c=[0.03, 0.75, 0.71, 0.64, 0.28, 0.28, 0.09, 0.19, 0.0, 0.19, 0.23, 0.19, 0.28, 0.13, 0.12, 0.06, 0.11, 0.77, 0.09, 0.14, 0.1, 0.21, 0.27, 0.26, 0.61, 0.18, 0.1, 0.16, 0.04, 0.2, 0.08, 0.05, 0.28, 0.22, 0.1, 0.26, 0.06, 0.04, 0.16, 0.87, 0.42, 0.2, 0.06, 0.19, 0.2, 0.07, 0.17, 0.04, 0.09, 0.18, 0.04, 0.09, 0.38, 0.07, 0.03, 0.07, 0.05, 0.08, 0.05, 0.05, 0.0, 0.18, 0.48, 0.2, 0.6, 0.25]
d=[0.77, 0.58, 0.57, 0.74, 0.41, 0.6, 0.59, 0.64, 0.63, 0.54, 0.73, 0.64, 0.6, 0.42, 0.53, 0.59, 0.57, 0.53, 0.86, 0.8, 0.77, 0.81, 0.3, 0.55, 0.53, 0.58, 0.56, 0.82, 0.43, 0.86, 0.52, 0.47, 0.42, 0.45, 0.47, 0.4, 0.5, 0.52, 0.5, 0.48, 0.49, 0.46, 0.42, 0.5, 0.51, 0.58, 0.49, 0.46, 0.52, 0.51, 0.4, 0.52, 0.42, 0.46, 0.52, 0.43, 0.48, 0.35, 0.44, 0.43, 0.43, 0.61, 0.65, 0.38, 0.42, 0.53]





    







plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #! 中文才不會亂碼 
plt.rcParams['axes.unicode_minus'] = False   #! 中文才不會亂碼




#print(data)
# plot 函式會取 column 值代表 y 軸的值，index 索引代表 x 軸
#axes = data.plot(kind='bar')


#myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')
# 設定標頭和字體
#plt.title('一月份各區域結婚數',fontproperties=myfont)
plt.title('水檢驗報告')
# 設定 x 軸標頭和字體
#plt.xlabel('區域別',fontproperties=myfont)
plt.xlabel('StationName:')
# 設定 y 軸標頭和字體
#plt.ylabel('結婚數')
#plt.ylabel('結婚數', fontproperties=myfont)
# 設定右上角說明圖示字體
#plt.legend(prop=myfont)
plt.legend()
plt.grid()   #會顯示格線
plt.xticks(rotation=90)  #!變更字體方向

# 使用 for 迴圈一一取出 x 軸標籤 label 設定字體，若 y 軸有中文字也是類似使用方式 get_yticklabels
# for label in axes.get_xticklabels():
#     #label.set_fontproperties(myfont)
#     label.set_fontproperties()

# 顯示圖表 not show in tkinker
#plt.show()
#產生Dataframe-------#data x > variable name
data = pd.DataFrame({'name': x , 'ph':b , 'sss':c, 'phsss':d})
data = data.set_index('name') #set data in name variable as  x 軸標籤
#產生Figuration-----
fig = Figure(figsize = (5, 5),  dpi = 100) 
plot1 = fig.add_subplot(111) 
axes = data.plot()
#
#plot1.plot(x, y1)  
#plot1.plot(x, y2, linestyle='-', color='r')
data.plot(x='name', ax=plot1)
#plot1.plot(myDframe)
#plot1.legend()
#plot1.grid()
#
canvas = FigureCanvasTkAgg(fig, master = win)   
canvas.get_tk_widget().grid(row=3, column=0, columnspan=3)
win.mainloop()