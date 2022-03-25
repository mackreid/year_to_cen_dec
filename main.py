from lookups import century_dict, decade_dict

def convert_year_to_str(year):
    # int(year) is to turn the year input (which is a string) into an int. the int() the full thing
    # is wrapped in just rounds the answer to the nearest int. eg. 1111 / 100 = 11.11 but we just want the whole int 11. 
    century = int(int(year) / 100)

    # here we are calculating how much time is left in the century to get the decade
    remaineder = int(year) - (century * 100)
    # then we do the same int() wrap thing to get decade - using the remainder 
    decade = int(int(remaineder) / 10)

    # catching any error in getting str's from the dict.
    # eg. year is 5478 and we don't have a key for 54 
    try: 
        centuryStr = century_dict[century]
        decadeStr = decade_dict[decade]
        return "%s %s" % (centuryStr, decadeStr)
    except:
        print('Something went wrong converting, rip.')


print('Welcome to the year to century and decade converter.')
print('I have no idea why this would be useful - but here we are :)')

yearInput = input('Please enter a year: ')
print(convert_year_to_str(yearInput))
