"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

# get the weight of the user on earth
weight = input("What is your weight on earth?>>>")
# change the datatype into int
weight = int(weight)
# define the function
def moon(weight):
    """get the weight on the moon by calculating the weight on the earth"""
    weight_on_moon = weight * 0.165
    return weight_on_moon


print(moon(weight))
