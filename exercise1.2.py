
#print the complementing DNA

#Tells the user what the program does
print("This program will print the complementing DNA sequence.")

#the sequence to count
sequenceOrigional = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#this asks the user for the code
##sequence = input('What is your DNA code?')
#changes overwrites the variable with an uppercase version
##sequence = sequence.upper()
##print(sequence.upper())

#changing the a's to b's. Uses b as a place holder while t is changed
sequenceComplement = sequenceOrigional.replace('A', 'B')
#changing t to a
sequenceComplement = sequenceComplement.replace('T', 'A')
#changing b's to t's
sequenceComplement = sequenceComplement.replace('B', 'T')
#repeating the progress with c's and g's using d as a placeholder
sequenceComplement = sequenceComplement.replace('C', 'D')
sequenceComplement = sequenceComplement.replace('G', 'C')
sequenceComplement = sequenceComplement.replace('D', 'G')

#Prints the origional sequence then the complementing sequence
print('\nThe original sequence is:', sequenceOrigional)
print('The complement Sequence is:', sequenceComplement)
