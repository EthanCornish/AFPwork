
#print the complementing DNA

#Tells the user what the program does
print("This program will print the complementing DNA sequence.")

#the sequence to count
#sequenceOrigional = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#this asks the user for the code
sequenceOrigional = input('What is your DNA code?')
#changes overwrites the variable with an uppercase version
sequenceOrigional = sequenceOrigional.upper()

# Complements the DNA Bases to the lowercase letters then reverts them back to uppercase
sequenceComplement = sequenceOrigional.replace('A', 't')
sequenceComplement = sequenceComplement.replace('T', 'a')
sequenceComplement = sequenceComplement.replace('C', 'g')
sequenceComplement = sequenceComplement.replace('G', 'c')
sequenceComplement = sequenceComplement.upper()

#Prints the origional sequence then the complementing sequence
print('\nThe original sequence is:', sequenceOrigional)
print('The complement Sequence is:', sequenceComplement)
