# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:48:50 2020

@author: MRUTYUNJAY BISWAL
"""


# object itself is the implicit super class in python
# it does almost nothing
# when we define a class, object is the default super class
# remeber using the following notation/syntax for creating a class
class kyaKarega(object):
    pass


print(kyaKarega.__class__)
# output => <class 'type'>

print(kyaKarega.__base__)
# output => <class 'object'>

"""
The base class object: __init__() method
"""
'''
The fundamentals of any object lies in three fragments:
    1. Creation 
    2. Initialization
    3. Destruction
    
You can say it as CID. Let's go through initialization first.
_______________________________________________________________
The superclass of all classes, object, has a default implementation of __init__()
that amounts to pass. We aren't required to implement __init__(). If we don't
implement it, then no instance variables will be created when the object is
created. In some cases, this default behavior is acceptable.

Consider the following example. The class required two instance variables, but doesn't
initialize them.
'''


class Rectangle:

    def area(self) -> float:
        return self.length * self.height


# let's play around our Rectangle class
# instantiate an object from the class
rec = Rectangle()
rec.length, rec.height = 5, 10
print(rec.area())

# However, we should avoid this kind of implicit use of instance variables as
# these may lead to poor polymorphism.
