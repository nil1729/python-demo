## Errors and Exceptions in Python

- Errors are bound to happen in our Code!
- Especially when someone else ends up using it in an unexpected way.
- We can use error handling to attempt to plan for possible errors.
    - For example, a user may try to write to a file that was only open in **mode="r"**.
- Currently if there is any type of error in our code, the entire script will stop.
- We can use Error Handling to let the script continue with other code, even if there is an error.
- We use three keywords for this:
    - **try**: This is the block of code to be attempted (may lead to an error).
    - **except**: Block of Code will execute in case there is an error in **try** block.
    - **finally**: A final block of code to be executed, regardless of  an error.

## Testing Using Pylint

- First install pylint  
    ```
    >> pip install pylint
    ```
- Create files and test by Run this Code    
    ```
    >> pylint file_name.py
    ```