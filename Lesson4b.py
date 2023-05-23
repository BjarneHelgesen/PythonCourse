class Car:
    def __init__ (self, model, year, price):
        self.model = model
        self.year = year
        self.price_history = []
        self.price = price # call to "self.price(price)"
        
    @property
    def price(self):
        return self._price
    
    @price.setter    
    def price(self, price):
        self.price_history.append(price)
        self._price = price

wreck = Car("Toyota Camry", 1986, 25000)
print(wreck.price) 

wreck.price = 20000
wreck.price = 15000
wreck.price = 10000
