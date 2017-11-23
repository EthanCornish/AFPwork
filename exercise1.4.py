
# Slicing out Introns

# The sequence being used
sequence = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCG' \
           'ATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

# Finding the two exons,    notation used is 'string[start:end]' note start is inclusive, end is not
exon1 = sequence[0:65]
exon2 = sequence[91:len(sequence)]

# Printing the final output
print('The coding sequence is.')
print(exon1 + exon2)


#Finding the percentage of the coding DNA to the full sequence
codingpercent = (((len(exon1) + len(exon2)) / len(sequence)) * 100)
print('\nThe coding part of the DNA makes up {0}% of the total sequence.\n'.format(round(codingpercent, 2)))

#Showing the coding part captalised and the non-coding part in lowercase
#The intron is in lowercase and the part inbetween the two parts
intron = sequence[65:90]
intron = intron.lower()
print(exon1 + intron + exon2)
