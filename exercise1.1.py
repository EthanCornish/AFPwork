
#find % of GCs

#Tells the user what the program does
print("This program will tell the user the GC content of a DNA sequence")

#the sequence to count
##sequence = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#this asks the user for the code
sequence = input(print('What is your DNA code?'))
#upper function does not appear to work, .capitalised tried as well but did not work
sequence.upper()
print(sequence)

#counts the number of C's and return s
numC = sequence.count('C')
print('C =', numC)

#counts the number of G's and returns
numG = sequence.count('G')
print('G =', numG)

#finds how many characters are in the code
length = len(sequence)
print('length =', length)

#Calculates the percentage
percentGC = (((numC + numG)/length) * 100)

#the round part rounds it too 2 decimal points
print('The GC content of the sequence is {0}%.'.format(round(percentGC, 2)))
