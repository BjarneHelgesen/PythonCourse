## What are classes?
Classes are custom data types. These data types can be similar to built in-data types, (e.g. `int, float, list, tuple, string,` etc.), it can model things from real life, such as books, customers, webpages, databases, text fields, it have some convenience functionionality (e.g. integer 0 to 59 which wraps around), or other uses.     

Classes typically work well to encapsulate (and hide implementation details of) high-level abstractions. 

In order to create objects of a given type (built-in type or class), a constructor are called. A constructor is the class or type name with paranethesis, and may contain parameters if the class accepts parameters for initialization. 
Examples:  
```Python
value = int("123")
rect = Rectangle(10, 10)
narnia = Book(“CS Lewis”, “Narnia Chronicles”, 1950)
cancel = Button(“Cancel”)
```

Built-in types also support implicit initialization, where the object value is inferred. This is not supported for classes, where calling a constructor is the only way to create an object of that class.

Objects are typically a collection of variables (called attributes) and functions (called methods) that operate on the attributes and/or parameters. Methods and attributes are referenced by object name, full stop and then attribute or method name. 

The example below uses the `__doc__` attribute and the `sort` and `append` methods of a list. 
```Python
mylist = [1,3,2,5,7] # Create a list using implicit intialization 
print("mylist doc string:", mylist.__doc__) 
mylist.sort()        # Sorts the list in-place => [1,2,3,5,7]
mylist.append(4)     # Append 4 to the list.   => [1,2,3,5,7,4]
```

Attributes and methods can be set using the same syntax, e.g. 
```Python
customer = Customer() 
customer.name = "John Doe" # if the attribute "name" does not exist, it will be created.
```

Classes are mutable by default, so assigning a varable to be equal to another class makes both variables point to the same object. In the example below, we assume that a class called TechniClass has been declared
 
```Python
techni_class1 = TechniClass()
techni_class1.mydata = 5
techni_class2 = techni_class1
techni_class2.mydata = 6
print(techni_class1.mydata) # prints 6 (not 5)
```
In order to debug problems with multiple variables are pointing to the same mutable object, the memory address of the objects can be used. `id()` and `is` are the standard ways to check for this in Python. 
```Python
address = id(my_object)  # id() returns the address of an object
if object1 is object2:   # is checks if two variables point to the same object. Syntactic sugar for id(object1) == id(object2)
    ...
```

## Class declaration and initialization
The minimal class declaration is as follows: 
```Python
class <class name>:
    ...
```

In order to initalize an object of the given class, an `__init__` method is declared. The parameters to it will be self (the new object) and all parameters given to the constructor. The parameters to `__init__` are often saved as attributes to make them available later. E.g. a circle class that is intialized with center coordinates and radius could look like this: 
```Python
class Circle: 
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
```


## Polymorphism and Duck Typing
Classes support polymorphism; Python  parameters and other variables don't have to be a specific type as long as they have the required attributes and methods. 
```Python
def add(a, b): 
    return a + b
```
The function above will add ints, floats and complex numbers. It will also concatename strings, lists, tuples as they all have defined behaviour for the plus operator.  

It is a common practice to declare several classes which implement a given interface (a set of attributes and methods), but this interface does not have to be formally defined or enforced. E.g. shapes (circles, squares, rectangles, parallelograms, rhombuses, ellipses, triangles, trapezoids, pentagons, etc.) could conform to an in interface, such as having methods `area()` and `circumference()`. The code using them does not have to know which type they are, as long as they conform to this informal interface.

The term Duck Typing comes from the Python practice of not enforcing that a parameter to a function conforms to a given interface before running the code. The Python philosophy is that if the code succeeds, the type was correct. "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 

