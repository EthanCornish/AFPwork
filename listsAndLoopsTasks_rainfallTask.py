
# WIP

# Makes a list, asks the user for CSVs
mRainfall = []
input = input('Please give the monthly rainfalls.\nSeparate each value using a comma but no whitespace.'
              'You may use decimals. E.g. 2,21,19.6')
mRainfall = input.split(',')    # Splits the input into the list at commas


# Works out the total
total = 0
for x in mRainfall:
    total += float(x)
print('The total is {0}°.'.format(total))

# Works out the average
average = (total/len(mRainfall))
print('The average is {0}°.'.format(round(average, 2)))



# Creates a min and max variable to allow the .format to work
minF = mm[0]
maxF = mm[-1]

# Uses the first value as the minimum thanks to the sort
print('The minimum temperature is {0}°.'.format(minF))
# The index value of -1 is a way of grabbing the last value
print('The maximum temperature is {0}°.'.format(maxF))
