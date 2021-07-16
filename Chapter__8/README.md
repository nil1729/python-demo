## Decorators

- A decorator is **a design pattern** in Python that allows a user to add new functionality to an existing object without modifying its structure.
- Decorators are usually called before the definition of a function we want to decorate.
- Example
  - Now we want to add some new capabilities to the function:
    ```
    def simple_func():
        # want to do more stuff!
        # Do simple stuff return something
    ```
  - We now have two options:
    - Add that extra code (functionality) to our old function
    - Create a brand new function that contains the old code and then add new code to that function
  - Problems of these two options:
    - But what if we then want to remove that extra "functionality"
    - We would need to delete it manually or make sure to have the old function
    - **Can we do something better? Maybe an ON/OFF switch to quickly add this functionality to our function?**
- Python has **decorators** that allow us to tack on extra functionality to an existing function without modifying its code.
- They use the **@** operator and are then placed on top of the original function which we want to decorate.
- Now we can easily add an extra functionality with a decorator:
  ```
    @my_decorator
    def simple_func():
        # Do simple stuff return something
  ```
