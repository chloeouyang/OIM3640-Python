"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
# """

# # get the weight of the user on earth
# from session05.my_abs import my_abs_filter


# weight = input("What is your weight on earth?>>>")
# # change the datatype into int
# weight = int(weight)
# # define the function
# def moon(weight):
#     """get the weight on the moon by calculating the weight on the earth"""
#     weight_on_moon = weight * 0.165
#     return weight_on_moon
# #print the weight on moon
# print(moon(weight))


"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

#1. get the weight on earth and the planet used to calculate
#2. calculate the weight on that planet
#3. print the weight on that planet

weight_on_earth=float(input('What is your weight on earth?>>>'))
planet=input('What planet do you want to use to calculate?>>>')

def weight_on_planet(weight_on_earth,planet):
    """get the weight on earth and return the equivalent weight on that planet"""

    if planet == 'moon':
        weight_on_planet=0.165*weight_on_earth
    else:
        if planet == 'mars':
            weight_on_planet=0.378*weight_on_earth
        else:
                weight_on_planet=2.528*weight_on_earth
    return weight_on_planet

print(weight_on_planet(weight_on_earth,planet))

