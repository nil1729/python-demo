## Functions in Python

- **def keyword**
    - Creating a function requires a very specific syntax, including the **def** keyword, correct indentation and proper structure.
    - Syntax:   
        ``` 
                       A colon indicates an
                       upcoming indented block.
                       Everything indented is then
                       "inside" the function
                              |           
        def name_of_function(args..):
         |                 |  
        keyword telling   We decide on the
        Python this is a  function name, 
        function           "Snake casing"
        """
         Docstring explains function (Multiline String)
        """
        ```
    - Typically we use the **return** keyword to send back the result of the function, instead of just printing it out.
    - **return** allows us to assign the output of the function to a new variable.

## LEGB Rule

- L: Local - Names assigned in any way within a function (def or lambda), and not declared global in that function.
- E: Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
- G: Global(module) - Names assigned at the top-level of a module file, or declared global in a def within the file
- B: Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError,...