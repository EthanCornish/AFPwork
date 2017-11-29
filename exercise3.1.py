
# Processing DNA in a file

# Pseudocode
# Start
#   Open the file for reading
#   Open the file for writing
#   For each line in inFile
#        Fine length of line
#        Wanted = length - 15
#        Output wanted to screen
#        Output wated to outfile
# Stop


inFile = open('/Users/19ecornish/Downloads/exercise3.1_InputFile.txt')
outFile = open('exercise3.1_Output', 'w')

for line in inFile:
    length = len(line)
    cutPoint = (length - 14)
    trimmedSequence = line[:cutPoint]
    print('Processed sequence with length {0}'.format(cutPoint))
    outFile.write(trimmedSequence)