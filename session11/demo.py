def count_vowel(name):
    count = 0
    for letter in name:
        # if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        if letter in "aeiou":
            count += 1
    return count

print(count_vowel('chloeeee'))
# print(count_vowel(chloeeee))

def count_vowel(name,strange_letter):
    count = 0
    for letter in name:
        if letter in strange_letter:
            count += 1
    return count

print(count_vowel('chloeeee', 'zsxc'))