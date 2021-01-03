import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#x = np.linspace(0, 1, 100)
#y = x ** 3

x= ['貢寮淨水場', '平溪淨水場', '坪林淨水場', '石門淨水場', '大湳淨水場', '龍潭淨水場', '大湖淨水場', '大湖二場淨水場', '明德淨水場', '三水源淨水場', '公館淨水場', '四水源淨水場', '阿丹淨水場', '二崙淨水場', '西螺淨水場', '莿桐淨水場', '土庫淨水場', '平和淨水場', '南化淨水場', '潭頂淨水場', '楠玉淨水場', '鏡面淨水場', '內埔農工淨水場', '長治百合淨水場', '屏東農場淨水場', '禮納里淨水場', '澄清湖淨水場', '路竹淨水場', '嶺口淨水場', '小坪淨水場', '丸山淨水場', '東澳淨水場', '金洋淨水場', '柑仔坑淨水場', '寒溪淨水場', '碧候淨水場', '廣興淨水場', '澳花淨水場', '蘇澳淨水場', '大溪淨水場', '四季淨水場', '圳頭淨水場', '枕山淨水場', '松羅淨水場', '金面淨水場', '英士淨水場', '深溝淨水場', '龍潭淨水場', '清洲淨水場', '利嘉淨水場', '初鹿淨水場', '泰安淨水場', '黑森林淨水場', '土板淨水場', '大王淨水場', '加羅板淨水場', '正興淨水場', '安朔淨水場', '金崙淨水場', '愛國埔淨水場', '嘉蘭淨水場', '水母淨水場', '成功淨水場', '紅葉淨水場', '瑞豐淨水場', '關山淨水場']
y=[6.99, 7.54, 7.55, 7.97, 7.18, 7.95, 7.57, 7.47, 7.78, 7.2, 8.01, 7.02, 7.52, 7.81, 6.93, 8.07, 7.3, 7.48, 8.26, 8.27, 8.01, 7.88, 7.27, 7.86, 6.94, 6.41, 6.74, 7.25, 7.43, 7.69, 6.43, 7.23, 8.21, 7.6, 7.76, 7.67, 6.63, 7.68, 6.39, 7.75, 7.75, 7.35, 7.72, 7.26, 7.6, 7.01, 7.12, 7.31, 7.37, 8.33, 7.03, 8.19, 8.34, 7.56, 6.9, 7.48, 6.83, 7.08, 8.12, 7.7, 7.84, 7.68, 7.78, 8.28, 7.08, 7.91]

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #! 中文才不會亂碼 
plt.rcParams['axes.unicode_minus'] = False   #! 中文才不會亂碼
# plt.rcParams["font.family"] = "arial"                #全体のフォントを設定
# plt.rcParams["xtick.direction"] = "in"               #x軸の目盛線を内向きへ
# plt.rcParams["ytick.direction"] = "in"               #y軸の目盛線を内向きへ
# plt.rcParams["xtick.minor.visible"] = True           #x軸補助目盛りの追加
# plt.rcParams["ytick.minor.visible"] = True           #y軸補助目盛りの追加
# plt.rcParams["xtick.major.width"] = 1.5              #x軸主目盛り線の線幅
# plt.rcParams["ytick.major.width"] = 1.5              #y軸主目盛り線の線幅
# plt.rcParams["xtick.minor.width"] = 1.0              #x軸補助目盛り線の線幅
# plt.rcParams["ytick.minor.width"] = 1.0              #y軸補助目盛り線の線幅
# plt.rcParams["xtick.major.size"] = 10                #x軸主目盛り線の長さ
# plt.rcParams["ytick.major.size"] = 10                #y軸主目盛り線の長さ
# plt.rcParams["xtick.minor.size"] = 5                 #x軸補助目盛り線の長さ
# plt.rcParams["ytick.minor.size"] = 5                 #y軸補助目盛り線の長さ
# plt.rcParams["font.size"] = 14                       #フォントの大きさ
# plt.rcParams["axes.linewidth"] = 1.5                 #囲みの太さ

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
#fig.savefig('test_5.png', bbox_inches="tight", pad_inches=0.05)  # 画像を保存
plt.show()