
# Splitting Genomic DNA and Writing to a File

### The following code is taken from 1.4
# The sequence being used
#sequence = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCG' \
#           'ATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

# grabbing the file
sourcefile = open('/Users/19ecornish/Downloads/exercise2.1-sourcefile.txt')
sequence = sourcefile.read()
print(sequence)


# Finding the two exons,    notation used is 'string[start:end]' note start is inclusive, end is not
exon1 = sequence[0:65]
exon2 = sequence[90:]

### The following code is new

exercise21fileA = open('exercise2.1FileA', 'w')
exercise21fileA.write('The first exon is {0}'.format(exon1))
exercise21fileA.close()

exercise21fileB = open('exercise2.1FileB', 'w')
exercise21fileB.write('The second exon is {0}'.format(exon2))
exercise21fileB.close()
