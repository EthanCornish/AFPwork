# Ask the user for the files for each of the fragments
# Read the file to a variable
# Print the fragment for the user
fragment1 = open(input('Enter the file directory of the first DNA Fragment'))
fragment1 = fragment1.read()
print('Fragment 1 is',fragment1)
fragment2 = open(input('Enter the file directory of the second DNA Fragment'))
fragment2 = fragment2.read()
print('Fragment 2 is',fragment2)
fragment3 = open(input('Enter the file directory of the third DNA Fragment'))
fragment3 = fragment3.read()
print('Fragment 3 is',fragment3)
fragment4 = open(input('Enter the file directory of the fourth DNA Fragment'))
fragment4 = fragment4.read()
print('Fragment 4 is',fragment4)
fragment5 = open(input('Enter the file directory of the fifth DNA Fragment'))
fragment5 = fragment5.read()
print('Fragment 5 is',fragment5)
fragment6 = open(input('Enter the file directory of the sixth DNA Fragment'))
fragment6 = fragment6.read()
print('Fragment 6 is',fragment6)

print('\n')
# Create a counting variable
count = 0

# Start a while loop that will use the counting variable to loop five times
while count < 5:
    # Ask the user for the file directory of a suspect sequence
    sequence = open(input('Enter the file directory of the suspect sequence.'))
    # Reading the file to a Variable (sequence)
    sequence = sequence.read()
    # Searching the suspect for each fragment and finding the index value. If value = -1 then fragment is not present
    # sfl stands for Suspect Fragment Location
    sfl1 = sequence.find(fragment1)
    sfl2 = sequence.find(fragment2)
    sfl3 = sequence.find(fragment3)
    sfl4 = sequence.find(fragment4)
    sfl5 = sequence.find(fragment5)
    sfl6 = sequence.find(fragment6)

    # Checks each sfl variable to see if the fragment is present and prints which fragments are present
    print('The suspect sequence contains the following fragments')
    if sfl1 >= 0:
        print('Fragment 1 ({0})'.format(fragment1))
    if sfl2 >= 0:
        print('Fragment 2 ({0})'.format(fragment2))
    if sfl3 >= 0:
        print('Fragment 3 ({0})'.format(fragment3))
    if sfl4 >= 0:
        print('Fragment 4 ({0})'.format(fragment4))
    if sfl5 >= 0:
        print('Fragment 5 ({0})'.format(fragment5))
    if sfl6 >= 0:
        print('Fragment 6 ({0})'.format(fragment6))
    print('\n')
    count += 1

#/Users/19ecornish/Downloads/fragment1.txt
#/Users/19ecornish/Downloads/suspect1.txt