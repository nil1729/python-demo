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