prices ={"Apple":300,"Banana":80,"Mango":150}
prices["Grapes"]=400
prices["Banana"]=90

print("Prices:",prices)
print("Prices of Apple:",prices["Apple"])

for fruit, price in prices.items():
    print(fruit,"costs",price,"Taka per kg")