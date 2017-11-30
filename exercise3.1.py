
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

# Opening the files for input and output
inFile = open('/Users/19ecornish/Downloads/exercise3.1_InputFile.txt')
outFile = open('exercise3.1_Output', 'w')

# Going through each line in the file
for line in inFile:
    # Finds the length of the line
    length = len(line)
    # Cuts the line at the right spot
    trimmedSequence = line[14:length]
    # Prints the length
    print('Processed sequence with length {0}'.format(trimmedSequence))
    # Saves the trimmed sequence to the output file
    outFile.write(trimmedSequence)
