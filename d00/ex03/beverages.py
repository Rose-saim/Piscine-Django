class HotBeverage:
    name = "hot beverage"
    price = 0.30
    description = "Just some hot water in a cup."

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description}"

class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    description = "A coffee, to stay awake."

class Tea(HotBeverage):
    name = "tea"
    price = 0.30
    description = "Just some hot water in a cup."

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    description = "Un po’ di Italia nella sua tazza!"
