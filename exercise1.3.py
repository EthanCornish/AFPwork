
# Restriction Fragment Lengths
print("This program will cut the DNA sequence at 'G*AATTC' and provide the size of each fragment.")

#The sequence
sequence = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

#Finds the index value of where the program should cut
cutpoint = (sequence.find('GAATTC'))

#Finds the size of the first fragment
size1 = cutpoint + 1
#Finds the size of the second fragment
size2 = (len(sequence) - size1)

#len(sequence) = the total length

#Gives the final output
print('The first fragment is {0} bases long.\nThe second fragment is {1} bases long.'.format(size1,size2))