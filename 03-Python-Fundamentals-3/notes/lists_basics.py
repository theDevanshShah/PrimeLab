drinks = ["coffee","tea","wine","juice","blood"]
print(drinks)

print(len(drinks))

drinks.pop()
print(drinks)

drinks.append("buttermilk")
print(drinks)

drinks.append("1")
print(drinks)

drinks.append("0.1")
print(drinks)

drinks.sort()
print(drinks)

drinks.extend("boba")

drinks.reverse()

print(drinks.index("tea"))
print(drinks)

mydrinks = drinks.copy()
print(mydrinks)

mydrinks.clear()
print(mydrinks)

print(drinks.count("period blood"))