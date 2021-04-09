## Basic Data Types ( Python )
| Name            | Type  | Description                                                       |
| --------------- | ----- | ----------------------------------------------------------------- |
| Integers        | int   | Whole Numbers such as 3, 300, 400                                 |
| Floating Points | float | Numbers with a decimal point 2.3, 4.5, 70.0                       |
| Strings         | str   | Ordered sequence of charecters: "Hello", "Nilanjan", "300"        |
| Lists           | list  | Ordered sequence of Objects: [10, "Hello", 20.4]                  |
| Dictionaries    | dict  | Unordered Key:Value pairs: {"myKey": "value", "name": "Nilanjan"} |
| Tuples          | tup   | Ordered immutable sequence of Objects: (10, "hello", 30.8)        |
| Sets            | set   | Unordered collection of unique objects: {"a", "b"}                |
| Booleans        | bool  | Logical value indicating **True** or **False**                    |

---
## Variables

**Rules For variable names**
- Names can not start with a Number
- There can be no spaces in the name, use _ (underscore) instead
- Can't use any of these symbols `:'"<>/?\()@#$%^&*~-+`
- It's considered best practice (PEP8) that names are lowercase.
- Avoid using words that have special meaning in Python like "list" and "str".

**Important Points**
- Python uses `Dynamic Typing`
- This means we can reassign variable to different data types.
- This makes Python very flexible in assigning data types, this is different than other languages that are `Statically-Typed`.
- **Pros of Dynamic Typing**
  - Very easy to work with
  - Faster development time
- **Cons of Dynamic Typing**
  - May result in bugs for unexpected data types.
  - You need to be aware of **type()**

---

## Strings

- Strings are sequence of charecters using the syntex of either single quotes or double quotes
  - "hello"
  - 'Nilanjan'
  - "I don't know Django"
- Because strings are ordered sequences means we can using **indexing** and **slicing** to grab sub-sections of the strings.
- Indexing notation uses [] notation after the string ( or variable assigned the String )
- Indexing allows you to grab a single character from the string ...
- **Indexing**
  - This actions use [] square brackets and number index to indicate positions of what we wish to grab
    - ```
        Charecters:    H  E  L  L  O
        Index:         0  1  2  3  4
        Reverse Index: 0 -4 -3 -2 -1 
      ```
- **Slicing**
  - Slicing allows us to grab a subsection of multiple charecters, a "slice" of the string.
  - This has the following syntex
    - **[start:stop:step]**
  - **start** is the Numeric index for the slice start
  - **stop** is the index we will go up to (but not include)
  - **step** is the size of the "jump" we take.
 
 ---
 
 ## Lists
 
 - Lists are ordered sequences that can hold a variety of Object Types.
 - They use [] brackets and commas to separate objects in the list.
    - [1, 2, 3 , 4]
 - Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off them.  
 
 ---
 
 ## Dictionaries
 
 - Dictionaries are unordered mappings for storing Objects. Previously we saw how lists store Objects in an ordered sequence, dictionaries use a key-value pairing instead.
 - This key-value pair allows users to quickly grab Objects without needing to know an index location.
 - Dictionaries use curly braces and colons to signify the keys and their associated values.  
        `{ "key1": 'value1', "key2": 'value2' }`
 - **So when to Choose a list and when to choose a dictionary ?**
    - **Dictionary**: 
        - Objects retrieved by `key name`.
        - Unordered and cannot be sorted.
    - **Lists**
        - Objects retrieved by `location`.
        - Ordered sequence can be indexed or sliced.
        
---

## Tuples

- Tuples are very similar to lists. However they have one key difference - **immutability**.
- Once an element is inside a tuple, it can not be reassigned.
- Tuples use parenthesis: `(1, 2, 3)`
- Special Methods: `index('item')` & `count('item')`

## Sets

- Sets are unordered collections of unique elements.
- Meaning there can only be one representative of the same Objects.
- **Initialization**    
    ```
    >> mySet = set()
    >> mySet # {item1, item2, ...}
    ```

---

## Booleans

- Booleans are operators that allows us to convey **True** or **False** statements.

---