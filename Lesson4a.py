from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def get_ticket_price(self):
        pass

class Bus(vehicle):
    def get_ticket_price(self):
        return 42

class Train(vehicle):
    def get_ticket_price(self):
        return 99


t = Train()
print(t.get_ticket_price())

b = Bus()
print(b.get_ticket_price())