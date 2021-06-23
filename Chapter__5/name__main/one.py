# ONE.PY File

def method_one():
    print("I am from One.py and I am Method One")

def method_two():
    print("I am from One.py and I am Method Two")
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    # Running this script directly
    # Execute functions (Code Organization)
    print("ONE.PY IS RUNNING DIRECTLY")
    method_one()
    method_two()
else:
    print("ONE.PY IS IMPORTED")