# Turns cm to inches
#
#def main1():
#    print('This program will act as a metric to imperial converter.')
#    print('--------------------------------------------------------')
#    cm = int(input('Enter an amount of centimeters to be converted to inches'))
#    print((cm_to_inch(cm)))
#    m = int(input('Enter an amount of meters to be converted to yards'))
#    print(m_to_yard(m))
#   km = int(input('Enter an amount of kilometers to be converted to miles'))
#    print(km_to_mile(km))

# Converts cm to inches
def cm_to_inch (cm):
    inch = 2.54 * cm
    return inch

# Converts m to yards
def m_to_yard (m):
    yard = 0.9144 * m
    return yard

 # Converts km to miles
def km_to_mile (km):
    mile = 1.60934 * km
    return mile

#main1()