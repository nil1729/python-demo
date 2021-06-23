## Python Statements and Logical Operators.

- Let's begin to learn about **Control Flow**
- We often only want certain code to execute when a particular condition has been met.
- To control this flow of logic we use some keywords.
  - **if**
  - **elif**
  - **else**
- Control Flow syntax makes use of colons and indentations (Whitespace).
- This indentation system is crucial to Python and is what sets it apart from other programming languages.
- Syntax of an **if** Statement
  ```
  if some_condition:
      # execute some code
  elif some_other_condition:
      # do domething different
  else:
      # do something else
  ```

---

## For Loops in Python

- Many objects in Python are _"iterable"_, meaning we can iterate over every element in the object.  
   eg. Such as every element in a list or every character in a String.
- We can use for loops to execute a block of Code for every iteration.
- The term **iterable** means you can "iterate" over the object.  
   eg. For example we can iterate over every character in string, iterate over every item in a list, iterate over every keys in a dictionary.
- Syntax of a **for loop**

  ```
    my_iterables = [1, 2, 3]
    for item_name in my_iterables:
        print(item_name)
  >> 1
  >> 2
  >> 3
  ```

---

## While Loops in Python

- While loops will continue to execute a block of code while some condition remains True.
- Syntax of a While loop
  ```
    while <some_boolean_condition>:
        # do something
  ```
- We can combine with an else if we want:
  ```
    while <some_boolean_condition>:
        # do something
    else:
        # do something different
  ```
- **break, continue, pass**
  - We can use break, continue and pass statements in our loops to add additional functionality for various cases. The three statements are defined by:
    - **break**: Breaks out of the current closest enclosing loop.
    - **continue**: Goes to the top of the closest enclosing loop.
    - **pass**: Does nothing at all.
