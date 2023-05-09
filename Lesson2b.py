SMALL = "Small"
LARGE = "Large"

SMALL_PRICE = 50
SMALL_TOPPING = 10
LARGE_PRICE = 100
LARGE_TOPPING = 20

class Pizza:
    def __init__(self, size):
        """size is SMALL or LARGE"""
        self.toppings = []
        if size not in (SMALL, LARGE):
            raise ValueError
        self.size = size

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calc_price(self, crust_price, topping_price):
        return crust_price + topping_price * len(self.toppings)
    
    def price(self):
        if self.size == SMALL:
            return self.calc_price(SMALL_PRICE, SMALL_TOPPING)
        return self.calc_price(LARGE_PRICE, LARGE_TOPPING)
    
    
my_pizza = Pizza(LARGE)
my_pizza.add_topping("Mozzarella")
my_pizza.add_topping("Pepperoni")
print(my_pizza.price())
print(my_pizza.toppings)