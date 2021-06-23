# First Lesson (Reading File)
# while True:
#     with open('files/demo.txt') as my_file:
#         content = my_file.read()
#         print(content)


# Second Lesson (Reading File and pause the execution for 10 secs)
# import time # built-in module
# while True:
#     with open('files/demo.txt') as my_file:
#         content = my_file.read()
#         print(content)
#     time.sleep(10)

# Third Lesson (File Existence Check):
# import time # built-in module
# import os # Standard module
# while True:
#     if os.path.exists('files/demo.txt'):
#         with open('files/demo.txt') as my_file:
#             content = my_file.read()
#             print(content)
#     else:
#         print("File not found")
#     # Delete the file to test
#     time.sleep(10)

# Fourth Lesson (Using Third Party Package) (Pandas)
import pandas
import time
import os
while True:
    if os.path.exists('files/data.csv'):
        my_data = pandas.read_csv('files/data.csv')
        print(my_data.mean())
    else:
        print("File not found")
    # Delete the file to test
    time.sleep(10)