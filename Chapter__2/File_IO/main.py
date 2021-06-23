# Reading File
my_file = open('demo.txt')
print(my_file.read())
my_file.close()

with open('demo.txt') as my_file:
    content = my_file.read()
print(content)


# Writing File
with open('test.txt', 'w') as test_file:
    test_file.write('Hello World\nPython 3')

with open('test.txt', 'w') as test_file:
    test_file.write('Hello\nPython')
    test_file.write('\nDjango')


# Appending a new Text to an existing file
with open('test.txt', 'a') as test_file:
    test_file.write('\nPandas')


with open('test.txt', 'a+') as test_file:
    test_file.write('\nNumpy')
    content = test_file.read()
    print(content)

with open('test.txt', 'a+') as test_file:
    test_file.write('\nFlask')
    test_file.seek(0)
    content = test_file.read()
    print(content)
