

# Create a counting variable
count = 0

fragment1 = 'TGAC'
#sourceFile_fragment = open(input('Enter the file directory of the first DNA Fragment'))
print(fragment1)
fragment2 = 'ACCG'
#sourceFile_fragment = open(input('Enter the file directory of the second DNA Fragment'))
print(fragment2)
fragment3 = 'GGCTG'
#sourceFile_fragment = open(input('Enter the file directory of the third DNA Fragment'))
print(fragment3)
fragment4 = 'CTACG'
#sourceFile_fragment = open(input('Enter the file directory of the fourth DNA Fragment'))
print(fragment4)
fragment5 = 'ATTGCC'
#sourceFile_fragment = open(input('Enter the file directory of the fifth DNA Fragment'))
print(fragment5)
fragment6 = 'GCATTA'
#sourceFile_fragment = open(input('Enter the file directory of the sixth DNA Fragment'))
print(fragment6)






# Start a while loop to add the sequences to the list
while count < 5:
    # Getting the file from the user (sequence)
    sourceFile_sequence = open(input('Enter the file directory of the suspect sequence.'))
    # Reading the file to a Variable (sequence)
    sequence = sourceFile_sequence.read()
    print(sequence)
    suspect1FragLocation1 = sequence.find(fragment1)
    suspect1FragLocation2 = sequence.find(fragment2)
    suspect1FragLocation3 = sequence.find(fragment3)
    suspect1FragLocation4 = sequence.find(fragment4)
    suspect1FragLocation5 = sequence.find(fragment5)
    suspect1FragLocation6 = sequence.find(fragment6)

    print('The locations of DNA Fragment 1, 2, 3, 4, 5 and 6 in suspect sequence are at the index value,',
          suspect1FragLocation1, suspect1FragLocation2, suspect1FragLocation3, suspect1FragLocation4, suspect1FragLocation5,
          suspect1FragLocation6, 'respectively.\nNote if the inde value is -1 then the fragment is not in the suspect sequence.\n\n')
    count += 1

#/Users/19ecornish/Downloads/fragment1.txt
#/Users/19ecornish/Downloads/suspect1.txt