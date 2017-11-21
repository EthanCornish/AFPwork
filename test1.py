print("Hello World")

name = input('You?')
print(name)

age = int(input(print("Age?")))


#The comma simply outputs the result
print('Hello', name, age)

#The + tries to contruct a string to display
#and it will only work with int if they are
#converted to string first
print('Hello' + name + str(age))


#The {x} are placeholders. It grahs from the variables in the format
#Written how you want the code to work
print('Hello {0} you are {1} years old'.format(name,age))