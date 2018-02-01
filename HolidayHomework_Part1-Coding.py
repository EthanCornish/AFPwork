
# Getting the file from the user (sequence)
sourceFile_sequence = open(input('Enter the file directory of the suspect sequence.'))
# Reading the file to a Variable (sequence)
sequence = sourceFile_sequence.read()

# Getting the file from the user (fragment)
sourceFile_fragment = open(input('Enter the file directory of the DNA fragment.'))
# Reading the file to a Variable (fragment)
fragment = sourceFile_fragment.read()

#Finds the location of the fragment and saves it to a variable
fragLocation = sequence.find(fragment)

# Prints the location of the DNA fragment
print('The DNA fragment, {0}, is at index value {1} of the sespect sequence.'.format(fragment, fragLocation))