''' 数値を様々に加工して連結することもできます。'''
population = 3000000
b_rate = 8.5

print(f'東京の人口は{population:,}人で、出生率は{b_rate:-^10.2f}です。')

a = "今は"
b = 21
c = "世紀です。"
text = f"{a}{b}{c}"
print(text)

#? f文字列は、+演算子やformatメソッドを使う方法よりも処理速度が速く、よりPythonらしい書き方です。次のように、文字列も数値も、
#? 型を気にせずに連結することができます。