price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price:
    print(i)



print("============================")






price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price:
    price[i] = price[i] * 0.85 

print(price)




print("============================")




price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}

for i in price:
    price[i] = round(price[i] * 0.85, 2)

print(price)





print("============================")





price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}


new_price = {}
for i in price:
    new_price[i] = round(price[i] * 0.85, 2)

print(price)
print(new_price)



print("============================")



price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}



for i in price.items():
    print(i)




print("============================")






price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}



for key, value in price.items():
    print(key)
    print(value)








print("============================")


price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}


new = {}
for key, value in price.items():
    new[value] = key
print(new)






print("============================")


price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}




for value in price.values():
    print(value)





print("============================")

price = {"meat": 2, "bread": 1, "potato": 0.5, "water": 0.2}


new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)












print("============================")
print("============================")
print("============================")




a = input("Dastur yopilishi uchun Enterni bosing: \n")