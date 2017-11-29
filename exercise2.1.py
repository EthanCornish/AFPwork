
# Splitting Genomic DNA and Writing to a File

# grabbing the file
# sourcefile = open...     Uses the directory to find the file and grab its contents turning them into a string
#sourcefile = open('/Users/19ecornish/Downloads/exercise2.1-sourcefile.txt')

# Asks the users for the file
sourcefile=open(input('Please the file directory for the file you want to be red and split'))
# Reads the file and places its content into a variable as a string
sequence = sourcefile.read()

### The following code is taken from 1.4

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
