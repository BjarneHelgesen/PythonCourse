# Object oriented python course
The course builds on procedural Python. Below is the theory covered.  


## What are classes?
Classes are custom data types. These data types can be similar to built in-data types, (such as `int, float, list, tuple, string,` etc.), it can model things from real life, such as books, customers, webpages, databases, text fields, it have some convenience functionionality (e.g. integer 0 to 59 which wraps around), or other uses.     

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

Objects are typically a collection of variables (called attributes) and functions (called methods) that operate on the attributes and/or parameters. Methods and attributes are referenced by object name, full stop and then attribute or method name. All declared attributes and methods for an object can be listed using the `dir()` function:

```Python
print("This is a test string")
```

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
Methods on the class can access the attributes thorugh self.  
Other code can access the attributes through the object variable.  E.g. 
```Python
c = Circle(5, 10, 1) # Create a Circle object with c.center_x = 5, c.center_y = 10, c.radius = 1
print(c.radius) #prints 1
```

## Polymorphism and Duck Typing
Classes support polymorphism; Python  parameters and other variables don't have to be a specific type as long as they have the required attributes and methods. 
```Python
def add(a, b): 
    return a + b
```
The function above will add ints, floats and complex numbers. It will also concatename strings, lists, tuples as they all have defined behaviour for the plus operator.  

It is a common practice to declare several classes which implement a given interface (a set of attributes and methods), but this interface does not have to be formally defined or enforced. E.g. shapes (circles, squares, rectangles, parallelograms, rhombuses, ellipses, triangles, trapezoids, pentagons, etc.) could conform to an in interface, such as having attributes `center_x`, `centery_y` and methods `area()` and `circumference()`. The code using them does not have to know which type they are, as long as they conform to this interface. 

The term Duck Typing comes from the Python practice of not enforcing that a parameter to a function conforms to a given interface before running the code. The Python philosophy is that if the code succeeds, the type was correct. "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 


## Conditional removal
If code has many conditions (if statements, etc.) it if often possible to wrap that logic in a separate class. An initialized object of that class can then be referenced without any conditional in either class. 


## Magic Methods
Magic Methods are sometimes called DUNDER (short for Double UNDERscore) functions. We can implement these Magic Methods in our object, and Python will "magically"  understand how to use these. They are typically not  called explicitly.

We have already used Magic Methods __init__ (for initalizing an object) and __doc__ (doc string). 

There are more than 100 Magic Methods in Python. It is common to implment a selected few of them to give the class certain property. It is not common or useful to implement all. 


The following Magic Methods are for casting. They don't take any parameters apart from self, and return an object of the requested type.  When these are implemented, Python will be able to cast your object to different types. For instance, print() tries to cast its parameters to string. If the class supports casting to string, the class can control how it is printed. 

```Python
__bool__
__float__
__int__
__complex__
__str__

```

> **_Python internals_**: When Python encounters an operator, it converts it to a Magic Method call. 
Here is an example when  two objects of type C are added using the plus operator:  ```x = a + b``` is translated into ```x = C.__add__(a,b)```

The Magic Methods for basic operators are: 
```Python
__add__   +
__and__   &
__contains__ in 
__eq__ ==
__floordiv__ // 
__ge__ >=
__gt__ > 
__invert__ ~
__le__ < 
__lshift__ <<
__lt__ <
__mod__ % 
__mul__ * 
__ne__ !=
__neg__ - (unary)
__or__ |
__pow__ **
__rshift__ >>
__sub__ - 
s__truediv__ //
__xor__ ^ 
```
These need to be implemented on the leftmost operand. (There are other methods that can be implemented on the rightmost operand)
There are Magic Methods for in-place operators like +=, /= etc. These Magic Methods are prefixed with an i for in-place. Normally, it is not necessary 
    
   
   
## Decorators
Decorators modify the behaviour of functions/methods. They are typically written as @-sign plus decorator name on the line above the function declaration. Below is a function called ```myfunc``` with a decorator called ```log```.
```Python
@log
def myfunc():
    ...
```  
## Properties
The @property decorator converts a method with only self as parameter to a property. Instances of this class can use the method name as if it was an attribute. Without a setter, this acts like a read-only attribute. Below is a read only property called ```incorporated_year```.
```Python
class Techni:
    @property
    def incorporated_year(self):
        return 1997
 
techni = Techni()
print(techni.incorporated_year)
```       
A setter is typically declared using a @method-name.setter decorator. In the example below, employed can be set to True or False. 
```Python
class Employee:
    def __init__(self):
        self._employed = True
        
    @property
    def employed(self):
        return self._employed
        
    @employed.setter
    def employed(self, value):
        if self._employed and not value:
            print("I lost my job")
        self._employed = value
```       
> **Python Convention:** Method/attribute names starting with underscore indicate that they are only meant to be used inside the class. Leading double underscores will mangle the name so that regular access from outside the class will fail.

## Inheritance
One class get the behavour (methods, attributes, properties, Magic Methods, etc. ) from another class. Below is an example where class B inherits from class A, and ```...``` represents some meaningful class definition.

```Python
class A:
   …

class B(A):
    …
```
 

Terminology: A is called the base class and b is claled the subclass 

When to use: When it is 100% clear that “B is an A”. Overuse of inheritace is a common problem in object oriented programming. 

## Abstract base classes
An abstract base class can be used to define an interface for a class. This can be used to enforce that all subclasses implement a certain behaviour. The abstract base class ```ABC```is defined in library ```abc```. Note that the library (abc) has a different capitalization from the class (ABC). The normal way to use it is to create a subclass of ```ABC``` and decorate the required methods in this class with ```@abstractmethod```. The implementation of these abstract methods can be just ```pass``` since they should never be executed. Below is an example that uses a ```Vehicle``` class as an ```ABC``` to enforce that all vehicles have a ```get_ticket_price()``` method.

```Python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_ticket_price(self):
	       pass

class Bus(Vehicle):
    def get_ticket_price(self):
        return 42

class Train(Vehicle):
    def get_ticket_price(self):
        return 99

	
def  print_ticket_price(transport):
    print(transport.get_ticket_price())

t = Train()
print_ticket_price(t)
```

## Python libraries
Python comes with more than 100 pre-installed libraries, listed at https://docs.python.org/3/library/ 

Tens of thousands of other libraries are stored as packages in Python's online package repository called PyPi and these can be installed with the **pip** executable. **pip** stands for Packages Installer for Python. The normal syntax is **pip install \<packagename\>** on the terminal.
> **If you have more than one Python installation on your computer:**  Execute **pip** from the Python installation you want it on; each installation has its own **pip** and its own set of libraries.  

E.g. in order to install the pygame library, execute: **pip install pygame** in the terminal. 
**pip** will locate pygame on https://PyPi.org and download/install it together with any dependencies.
