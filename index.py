#Comment
print("Hello World")

# print("生きたい")

# print("ノロノロビーム")

#演算
# print(11/2.0)

# 変数

# classとインスタンス
class Card:
    def __init__(self, date, user_name):
        self.date = date
        self.user_name = user_name
    def message(self):
        return "この投稿は" + self.user_name + "さんが" + self.date + "に投稿しました"

data_a = "2022-01-01"
user_name_a = "Taro"
card_a = Card(data_a,user_name_a)

data_b = "2022-01-01"
user_name_b = "Taro"
card_b = Card(data_b,user_name_b)

print(card_a.message())
print(card_b.message())
