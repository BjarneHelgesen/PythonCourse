## Lesson 1
Lesson1.py contains classes create shapes with a center point, a circumference and an area. center_distance.png contains an illustration of how to measure center distance. 

Extend Lesson1.py with one more shape and add one extra method to each shape (e.g. number of corners, total_width, or any other functionality)

## Lesson 2

Create a 2D vector class. This can be used to represent a force which has components in x and y direction. 

Create functions that 
* Adds two vectors
* Negates a vector 

Both functions should take vector(s) as parameter(s) and return a new vector.  

Here is an example of possible usage:
```Python

a = Vector(1,4)
b = Vector(-2, 5)

a_plus_b = add(a, b)
minus_a = negate(a)
```
---
Create a Pizza class which keeps track of the size and the toppings that are added. Any number of toppings can be added after construction. The price for a small pizza is 50 plus 10 per topping. For a large pizza, the price is 100 plus 20 per topping. 

```Python
my_pizza = Pizza("Large")
my_pizza.add_topping("Mozzarella")
my_pizza.add_topping("Pepperoni")
print(my_pizza.price())
```

Also make a function that lists the toppings

Are there better ways to create an interface for this? Please improve…

## Lesson 3
Modify your Pizza class as follows: Create a PizzaSize class for price info for a given Pizza size. 
Use an object of this class as a parameter during construction of the Pizza class to avoid if statements in the Pizza class

---
Make it possible to add to vectors using the ‘+’ operator by implementing these methods in the Vector class:
```Python
_ _str_ _(self) 
_ _add_ _(self, other)
```

Test code: 
```Python
q = Vector(1,2)
r = Vector(100, 200)
print(q + r)
```

## Lesson 4
Implement an Angle class which has properties for radians and degrees, where both can be read and set. Degrees go from 0 to 360, radians go from 0 to 2*PI. 

Here is test code 
```Python
import math

def test_angle():
    a = Angle() #gives default value of 0 to the angle. 
    a.radians = math.pi
    assert a.radians == math.pi
    assert a.degrees == 180 
    a.degrees = 17
    assert a.degrees == 17
    assert a.radians == 17/360*2*math.pi
    print("Test ok")
```    

## Lesson 5 
Modify lesson1.py to use an Abstract Base Class to enforce that all shapes have area() and circumference() methods. 

Modify Lesson 5b to make an object for the the rectangle so the main loop has less knowledge about implementation details.

## Lesson 6
Create function that takes two Elements from Lesson 6b and check if they collide (overlap). 


