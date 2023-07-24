stock ={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

shopping_cart = ["pear", "orange", "apple"]

shopping_cart = [("pear",1), ("orange", 3), ("apple",10)]

for i in shopping_cart:
    if stock[i[0]] - i[1] < 0:
        shopping_cart.pop(shopping_cart.index(i))
    else:
        stock[i[0]] -= i[1]

print("----------------")
print("     Bill")
print("----------------")
for i in shopping_cart:
    print(f"{i[0]} x{i[1]} @  £{prices[i[0]]}")
print("----------------")
print(sum([prices[i[0]] * i[1]  for i in shopping_cart]))
print("----------------")