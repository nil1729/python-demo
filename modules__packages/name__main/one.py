# ONE.PY File

def func_in_one():
    print("I am from One.py")

def function():
    print("Test Function()")
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    # Run this script
    # Execute functions (Code Organisation)
    function()
    print("ONE.PY IS RUNNING DIRECTLY")
else:
    print("ONE.PY IS IMPORTED")