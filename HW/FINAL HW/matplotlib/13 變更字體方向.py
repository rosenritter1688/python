import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讀入資料集檔案
df = pd.read_csv(r'C:\Users\Bruce Ashbee\Documents\Python\HW\FINAL HW\matplotlib\107年結婚對數.csv')
print(df)
print(type(df))

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #! 中文才不會亂碼 
plt.rcParams['axes.unicode_minus'] = False   #! 中文才不會亂碼

# loc 取值方式為 [索引, [欄位]]，取 月份區域別 出來當作 index
data = df.loc[:, ['月份區域別', '一月']]
#print(data)
# 原本 index 為 0, 1, 2, 3...12，改為 月份區域別，這樣 x 軸標籤就會改為 月份區域別
data = data.set_index('月份區域別')
#print(data)
# plot 函式會取 column 值代表 y 軸的值，index 索引代表 x 軸
#axes = data.plot(kind='bar')
axes = data.plot()

#myfont = FontProperties(fname=r'./NotoSansCJK-Black.ttc')
# 設定標頭和字體
#plt.title('一月份各區域結婚數',fontproperties=myfont)
plt.title('一月份各區域結婚數')
# 設定 x 軸標頭和字體
#plt.xlabel('區域別',fontproperties=myfont)
plt.xlabel('區域別')
# 設定 y 軸標頭和字體
plt.ylabel('結婚數')
#plt.ylabel('結婚數', fontproperties=myfont)
# 設定右上角說明圖示字體
#plt.legend(prop=myfont)
plt.legend()
plt.xticks(rotation=90)  #!變更字體方向

# 使用 for 迴圈一一取出 x 軸標籤 label 設定字體，若 y 軸有中文字也是類似使用方式 get_yticklabels
# for label in axes.get_xticklabels():
#     #label.set_fontproperties(myfont)
#     label.set_fontproperties()

# 顯示圖表
plt.show()