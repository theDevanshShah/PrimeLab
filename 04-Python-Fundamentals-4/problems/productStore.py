# Product Store
# Design & Create An Online Store For Products with 2 parameters name & price
# Track Total Products Being Created
# Calculate the discount on each product based on a % parameter.

# As we can see here first we have 2 params which are going to be different for all the products so we can save them in instance attributes.

class ProductStore:
    count = 0 # Class Level Attribute
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(name, price)
        ProductStore.count += 1
    
    @classmethod
    def trackingProducts(cls):
        return cls.count
    
    @staticmethod
    def calculatingDiscount(price, percentage):
        discountedAmount = price / 100 * percentage
        return discountedAmount

# Making Products
product_1 = ProductStore("Macbook",10_00_000)
product_2 = ProductStore("iPhone",1_00_000)
product_3 = ProductStore("shampoo",1000)

# Calculating Discount
print(f"The discounted amount for {product_1.name} will be : {product_1.calculatingDiscount(product_1.price, 10)}")
print(f"The discounted amount for {product_2.name} will be : {product_2.calculatingDiscount(product_2.price, 10)}")
print(f"The discounted amount for {product_3.name} will be : {product_3.calculatingDiscount(product_3.price, 10)}")

# Counting Total Products
count = ProductStore.count
totalCount = ProductStore.trackingProducts(count)
print(f"The Total Product Count Is : {totalCount}")