class Order():
    def __init__(self , item , price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

Order1 = Order("chips" , 20)
Order2 = Order("cake" , 15)

print(Order1 > Order2)