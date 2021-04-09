# TWO.PY File

import one

print("TOP LEVEL IN TWO.PY")

if __name__ == "__main__":
    print("TWO.PY IS RUNNING DIRECTLY")
    one.func_in_one()
else:
    print("TWO.PY IS IMPORTED")