## Object Oriented Programming

- Object Oriented Programming (OOP) allows programmers to create their own **objects** that have methods and attributes.
- We see that after defining a string, list, dictionary, or other objects, we are able to call methods off of them with the **.method_name()** syntax.
    - These methods act as a functions that use information about the object, as well as the object itself to return results, or change the current object.
    - For example this includes appending to a list, or counting the occurrences of an element in a tuple.
- **Syntax of OOP**  
   
        class NameOfClass():
            def __init__(self, param1, param2):
                self.param1 = param1
                self.param2 = param2
            def some_method(self):
                # perform some action
                print(self.param1)

