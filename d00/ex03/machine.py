import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.cups_served = 0
        self.broken = False

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        description = "An empty cup?! Gimme my money back!"

    def repair(self):
        print("Machine repaired.")
        self.cups_served = 0
        self.broken = False

    def serve(self, beverage_class):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()
        
        if self.cups_served >= 10:
            self.broken = True
            raise CoffeeMachine.BrokenMachineException()

        self.cups_served += 1
        if random.choice([True, False]):
            return beverage_class()
        else:
            return CoffeeMachine.EmptyCup()

# Test de la machine à café
if __name__ == "__main__":
    machine = CoffeeMachine()

    beverages = [Coffee, Tea, Chocolate, Cappuccino]

    try:
        for _ in range(12):  # Tentons de servir 12 boissons (la machine devrait se casser après 10)
            bev = machine.serve(random.choice(beverages))
            print(bev)
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
        machine.repair()  # Réparation après panne

    # Recommençons après réparation
    try:
        for _ in range(5):  # Tentons de servir encore quelques boissons
            bev = machine.serve(random.choice(beverages))
            print(bev)
    except CoffeeMachine.BrokenMachineException as e:
        print(e)
