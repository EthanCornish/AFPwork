
# Opens a file
file = open('Chapter3-ListsAndLoops-Tutorial#1')

# Goes through each line in the file
for line in file:
    # Prints the line while removing \n
    print(line.strip('\n'))
    # Creates a list \n and spliting after a whitespace
    words = line.strip('\n').split(' ')
    print(words)