
# Function Tutorial

# Creating a main function
# In the main function print instructions and ask for a value

def main():
    print('Hello')
    print('This program will ask you for a temperature\nin fahrenheit.')
    print('-----------------------------------------------------------')
    value = int(input('Enter a value'))
    # Calls the other function inside the main function
    print(ftoc(value))


# Create a function to convert fahrenheit to celsius
# All the function does is execute a specific job
def ftoc(fah):
    #fah = int(input('Enter a tempreature'))
    cel = (fah-32) * (5/9)
    # The :.2f is rounding it too 2dp
    print('{0}° Fahrenheight = {1:.2f}° Celcius'.format(fah, cel))
    return cel

# Runs the function
main()









