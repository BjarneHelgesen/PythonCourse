# Modifications to Lesson 2b 
# Using object orientation to avoid conditionals

class PizzaSize:
    def __init__(self, name, crust_price, topping_price):
        self.size_name =  name
        self.crust_price = crust_price
        self.topping_price = topping_price

# Create standard sizes to make creation simple 
LARGE = PizzaSize("Large", 100, 20)
SMALL = PizzaSize("Small", 50, 10)

class Pizza:
    """Calculates price and keeps track of toppings,etc."""
    def __init__(self, size):
        """size is an instance of PizzaSize, e.g. LARGE, SMALL"""
        self.toppings = []
        self.size = size

    def add_topping(self, topping):
        """Adds a topping to a pizza. 
        This may be called several times to add more toppings. 
        The same topping may be repeated. """
        self.toppings.append(topping)         
    
    def price(self):
        """Returns the price of the pizza with the current toppings. 
        May be called before all toppings are added"""
        return self.size.crust_price + self.size.topping_price * len(self.toppings)
    
my_pizza = Pizza(LARGE)
my_pizza.add_topping("Mozzarella")
my_pizza.add_topping("Pepperoni")

print(my_pizza.price())
print(my_pizza.toppings)