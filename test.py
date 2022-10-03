import twstock
from twstock import stock
print(twstock.__path__)
stock = twstock.Stock('2330')
bfp = twstock.BestFourPoint(stock)
print(bfp.best_four_point_to_buy())   # 判斷是否為四大買點

print(bfp.best_four_point_to_sell())  # 判斷是否為四大賣點

print(bfp.best_four_point())         # 綜合判斷
# print(bfp = twstock.BestFourPoint(twstock.Stock("2330")).best_four_point())