"""
----------------------------------------------------------------------
Q1. Please complete the following function to use your APIKEY to
get current wind speed in your current place
from openweathermap.org.

If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below,
but you will lose 10 points.

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
----------------------------------------------------------------------
"""
import urllib.request
import json

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)


def get_wind_speed():
    """
    Returns current wind speed in your current place
    from api.openweathermap.org
    """
    pass


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(get_wind_speed())

## Expected output:


"""
----------------------------------------------------------------------
Q2. 

The information is encoded in the DNA by the order of the arrangement 
of the bases (A, T, G, C). In a DNA sequence, the symbols "A" and "T" 
are complementary to each other, just like "C" and "G". You need to 
create a function to get the complementary side of a given DNA. 


NOTICE: you are required to use (not return) DICTIONARY for this question.
----------------------------------------------------------------------
"""


def reverse_DNA(data):
    """
    Given a DNA sequence (a string), return the complement DNA sequence
    """
    pass


# # Uncomment the following lines to test
# dna1 = "AAAA"
# dna2 = "ATTGC"
# dna3 = "GTAT"
# print(reverse_DNA(dna1))
# print(reverse_DNA(dna2))
# print(reverse_DNA(dna3))

## Expected output:
## TTTT
## TAACG
## CATA


"""
---------------------------------------------------------------------------------
Q3. Number of people in the subway

There is a Green Line subway train heading toward Boston, and it takes on and drops 
off people at every MBTA station.

You will be provided a list of integer tuples. Each integer tuple has two items 
representing the number of people who boarded the train and the number of people 
who got off at the MBTA station.

Create a function that returns the number of people who are still on the subway train 
after the last MBTA station (after the last tuple). Although it is the last station, 
the train is not empty, some people are still inside the train and they might be 
sleeping there :D

Check out the test cases to help you understand this problem
---------------------------------------------------------------------------------
"""


def people_in_train(data):
    """
    Given a list of int tuples, return an integer
    """
    pass


# # Uncomment the following lines to test
# passengers1 = [(100, 0), (30, 50), (50, 100)]
# passengers2 = [(26, 10), (20, 21), (16, 0), (18, 48)]

# print(people_in_train(passengers1))
# print(people_in_train(passengers2))

## Expected output:
## 30
## 1

"""
---------------------------------------------------------------------------------
Q4. covid-19-vaccine.json is a JSON file that contains vaccine information in MA.
 Please complete the function to read the city names into a list. Each city name 
 will be one item in the list. 
 
 Part of function is given. The JSON data is loaded into a variable, data, which is 
 a dictionary. Please do not change the existing code. 
---------------------------------------------------------------------------------
"""


def read_cities_to_list():
    """
    Return: a list of city names
    """
    import json
    import pprint

    # Make sure covid-19-vaccine.json is under "data" folder
    with open('data/covid-19-vaccine.json') as f:
        data = json.load(f)  # load json file into a dictionary named data
        pprint.pprint(data)
    # You can write code below


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(read_cities_to_list())


## Expected output:
# ['ABINGTON', 'AGAWAM', 'ALLSTON', 'AMHERST', 'ARLINGTON', 'ASHLAND', 'ATTLEBORO', 'BEDFORD', 'BELCHERTOWN', 'BELMONT', 'BILLERICA', 'BOSTON', 'BOURNE', 'BRAINTREE', 'BRIGHTON', 'BROCKTON', 'BROOKLINE', 'BURLINGTON', 'CAMBRIDGE', 'CHATHAM', 'CHELSEA', 'CHESTNUT HILL', 'CHICOPEE', 'COHASSET', 'CONCORD', 'DANVERS', 'DEDHAM', 'DORCHESTER', 'EAST BOSTON', 'EAST BRIDGEWATER', 'EAST FALMOUTH', 'EAST HARWICH', 'EVERETT', 'FALL RIVER', 'FOXBOROUGH', 'FRAMINGHAM', 'GEORGETOWN', 'GLOUCESTER', 'GRANBY', 'GREAT BARRINGTON', 'GREENFIELD', 'HADLEY', 'HANOVER', 'HANSON', 'HARWICHPORT', 'HAVERHILL', 'HINGHAM', 'HOLBROOK', 'HOLLISTON', 'HOLYOKE', 'HOPKINTON', 'HUDSON', 'HYANNIS', 'HYDE PARK', 'IPSWICH', 'KINGSTON', 'LANESBOROUGH', 'LAWRENCE', 'LEOMINSTER', 'LEXINGTON', 'LONGMEADOW', 'LOWELL', 'LYNN', 'MALDEN', 'MARBLEHEAD', 'MARLBOROUGH', 'MASHPEE', 'MAYNARD', 'MEDFIELD', 'MEDFORD', 'METHUEN', 'MIDDLEBOROUGH', 'MIDDLETON', 'MILFORD', 'MILLBURY', 'MILLIS', 'NEEDHAM', 'NEW BEDFORD', 'NEWTON', 'NORTH ANDOVER', 'NORTH ATTLEBOROUGH', 'NORTH DARTMOUTH', 'NORTH EASTON', 'NORTH GRAFTON', 'NORTHAMPTON', 'NORWELL', 'ORLEANS', 'OXFORD', 'PALMER', 'PEABODY', 'PLAINVILLE', 'PROVINCETOWN', 'QUINCY', 'RANDOLPH', 'READING', 'REVERE', 'ROSLINDALE', 'ROWLEY', 'SALEM', 'SALISBURY', 'SANDWICH', 'SAUGUS', 'SEEKONK', 'SHARON', 'SOMERVILLE', 'SOUTH EASTON', 'SOUTH HAMILTON', 'SOUTH WEYMOUTH', 'SOUTH YARMOUTH', 'SOUTHWICK', 'SPRINGFIELD', 'STONEHAM', 'STOUGHTON', 'STURBRIDGE', 'SWANSEA', 'TAUNTON', 'WALTHAM', 'WAREHAM', 'WATERTOWN', 'WAYLAND', 'WELLESLEY', 'WEST BRIDGEWATER', 'WEST NEWTON', 'WEST SPRINGFIELD', 'WESTBOROUGH', 'WESTFORD', 'WESTWOOD', 'WEYMOUTH', 'WILBRAHAM', 'WILMINGTON', 'WINCHENDON', 'WINCHESTER', 'WINTHROP', 'WOBURN', 'WORCESTER', 'WRENTHAM']


"""
--------------------------------------------------------------------------
Q5. Please complete the function that takes a list of city names, returns
a dictionary - in this dictionary, key is a letter and value is a list of 
city names that start with that letter. You can find example from the expected 
output below
--------------------------------------------------------------------------
"""


def first_letters(cities):
    """
    cities: a list of city names

    Return: a dictionary of letter: city pairs
    """
    pass


# When you've completed your function, uncomment the
# following lines and run this file to test!

# city_names = read_cities_to_list()
# print(first_letters(city_names))

## Expected output:
# {'A': ['ABINGTON', 'AGAWAM', 'ALLSTON', 'AMHERST', 'ARLINGTON', 'ASHLAND', 'ATTLEBORO'], 'B': ['BEDFORD', 'BELCHERTOWN', 'BELMONT', 'BILLERICA', 'BOSTON', 'BOURNE', 'BRAINTREE', 'BRIGHTON', 'BROCKTON', 'BROOKLINE', 'BURLINGTON'], 'C': ['CAMBRIDGE', 'CHATHAM', 'CHELSEA', 'CHESTNUT HILL', 'CHICOPEE', 'COHASSET', 'CONCORD'], 'D': ['DANVERS', 'DEDHAM', 'DORCHESTER'], 'E': ['EAST BOSTON', 'EAST BRIDGEWATER', 'EAST FALMOUTH', 'EAST HARWICH', 'EVERETT'], 'F': ['FALL RIVER', 'FOXBOROUGH', 'FRAMINGHAM'], 'G': ['GEORGETOWN', 'GLOUCESTER', 'GRANBY', 'GREAT BARRINGTON', 'GREENFIELD'], 'H': ['HADLEY', 'HANOVER', 'HANSON', 'HARWICHPORT', 'HAVERHILL', 'HINGHAM', 'HOLBROOK', 'HOLLISTON', 'HOLYOKE', 'HOPKINTON', 'HUDSON', 'HYANNIS', 'HYDE PARK'], 'I': ['IPSWICH'], 'K': ['KINGSTON'], 'L': ['LANESBOROUGH', 'LAWRENCE', 'LEOMINSTER', 'LEXINGTON', 'LONGMEADOW', 'LOWELL', 'LYNN'], 'M': ['MALDEN', 'MARBLEHEAD', 'MARLBOROUGH', 'MASHPEE', 'MAYNARD', 'MEDFIELD', 'MEDFORD', 'METHUEN', 'MIDDLEBOROUGH', 'MIDDLETON', 'MILFORD', 'MILLBURY', 'MILLIS'], 'N': ['NEEDHAM', 'NEW BEDFORD', 'NEWTON', 'NORTH ANDOVER', 'NORTH ATTLEBOROUGH', 'NORTH DARTMOUTH', 'NORTH EASTON', 'NORTH GRAFTON', 'NORTHAMPTON', 'NORWELL'], 'O': ['ORLEANS', 'OXFORD'], 'P': ['PALMER', 'PEABODY', 'PLAINVILLE', 'PROVINCETOWN'], 'Q': ['QUINCY'], 'R': ['RANDOLPH', 'READING', 'REVERE', 'ROSLINDALE', 'ROWLEY'], 'S': ['SALEM', 'SALISBURY', 'SANDWICH', 'SAUGUS', 'SEEKONK', 'SHARON', 'SOMERVILLE', 'SOUTH EASTON', 'SOUTH HAMILTON', 'SOUTH WEYMOUTH', 'SOUTH YARMOUTH', 'SOUTHWICK', 'SPRINGFIELD', 'STONEHAM', 'STOUGHTON', 'STURBRIDGE', 'SWANSEA'], 'T': ['TAUNTON'], 'W': ['WALTHAM', 'WAREHAM', 'WATERTOWN', 'WAYLAND', 'WELLESLEY', 'WEST BRIDGEWATER', 'WEST NEWTON', 'WEST SPRINGFIELD', 'WESTBOROUGH', 'WESTFORD', 'WESTWOOD', 'WEYMOUTH', 'WILBRAHAM', 'WILMINGTON', 'WINCHENDON', 'WINCHESTER', 'WINTHROP', 'WOBURN', 'WORCESTER', 'WRENTHAM']}


"""
--------------------------------------------------------------------------
Q6.(10 bonus points) Write a function that prints the dictionary from Q5. 
Your function should first print the longest list of cities with same first 
letter, followed by the second longest, and so on. 
--------------------------------------------------------------------------
"""
