
# Uses the previously made functions in a menu

import functionsTasks_functionPractice as flib


# The function main gives the user instructions and runs the bulk of the code
def main():
    print('This program is a metric to imperial converter.')
    print('-----------------------------------------------')
    # Runs the main part of the code
    menu()

def menu():
    # Creates a variable to store the users response and runs the while loop
    choice = '0'
    while choice == '0':
        print('Enter "1" to convert centimeters to inches.')
        print('Enter "2" to convert meters to yards.')
        print('Enter "3" to convert kilometers to miles.')
        print('Enter anything else to quit the program')
        choice = input()
        if choice == '1':
            cm = float(input('Enter an amount of centimeters to be converted to inches.'))
            inch = flib.cm_to_inch(cm)
            print('{0}cm is equal to {1:.2f}inch\n'.format(cm, inch))
            menu()
        elif choice == '2':
            m = float(input('Enter an amount of meters to be converted to yards.'))
            yard = flib.m_to_yard(m)
            print('{0}cm is equal to {1:.2f}inch\n'.format(m, yard))
            menu()
        elif choice =='3':
            km = float(input('Enter an amount of kilometers to be converted to miles.'))
            mile = flib.km_to_mile(km)
            print('{0}km is equal to {1:.2f}miles.\n'.format(km, mile))
            menu()
        else:
            print('You did not enter 1, 2 or 3.\nThe program has ended.')
main()
