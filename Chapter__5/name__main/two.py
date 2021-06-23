# TWO.PY File

import one

print("TOP LEVEL IN TWO.PY")

if __name__ == "__main__":
    print("TWO.PY IS RUNNING DIRECTLY")
    one.method_one()
    one.method_two()
else:
    print("TWO.PY IS IMPORTED")