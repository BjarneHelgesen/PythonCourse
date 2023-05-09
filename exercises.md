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
Create a Pizza class which keeps track of the size and the toppings that are added. Any number of toppings can be added after construction. The price for a small pizza is 50 plus 10 per topping. For a large, the price is 100 plus 20 per topping. 

```Python
my_pizza = Pizza("Large")
my_pizza.add_topping("Mozzarella")
my_pizza.add_topping("Pepperoni")
print(my_pizza.price())
```

Also make a function that lists the toppings

Are there better ways to create an interface for this? Please improve…

