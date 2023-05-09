SMALL = "Small"
LARGE = "Large"

SMALL_CRUST = 50
SMALL_TOPPING = 10
LARGE_CRUST = 100
LARGE_TOPPING = 20

class Pizza:
    def __init__(self, size):
        """size is SMALL or LARGE"""
        if size not in (SMALL, LARGE):
            raise ValueError
        self.toppings = []
        self.size = size
        if size == LARGE:
            self.crust_price = LARGE_CRUST
            self.topping_price = LARGE_TOPPING
        else:
            self.crust_price = SMALL_CRUST
            self.topping_price = SMALL_TOPPING

    def add_topping(self, topping):
        self.toppings.append(topping)        
    
    def price(self):
        return self.crust_price + self.topping_price * len(self.toppings)
        
    
my_pizza = Pizza(LARGE)
my_pizza.add_topping("Mozzarella")
my_pizza.add_topping("Pepperoni")
print(my_pizza.price())
print(my_pizza.toppings)