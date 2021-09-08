# name=input("Please enter your name")
# print('hello',name)

# year=input("Please enter your year of birth>>>")
# print(2021-year)

# 1.ask user to enter the year of birth, expecting user to enter an integer
year = input('Which year were you born?>>>')
# 2.store the integer to a variable, year
# 2.1 convert the variable to an integer
year=int(year)
# 3. calculate the age, 2021-year
age=2021-year
# 4. store the result to another variable, age
# 5. print the age
print('You must be',age,'years old.')

