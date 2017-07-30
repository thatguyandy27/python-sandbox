# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


f = 0
# print(f)

# f = "abc"
# print(f)


# print("String type: " + str(123))


def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)
print(someFunction())
print(someFunction)


def func2(arg1, arg2):
    print(arg1, " ", arg2)


func2(10, 20)
print(func2(10, 20))


def cube(x):
    return x*x*x

print(cube(3))
