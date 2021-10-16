t = ['a', 'b', 'c']

# append
t.append('e')
# ['a', 'b', 'c', 'e']
print(t)

t.append('d')
# ['a', 'b', 'c', 'e', 'd']
print(t)

# reverse
t.reverse()
# ['d', 'e', 'c', 'b', 'a']
print(t)

# sort
t.sort()
# ['a', 'b', 'c', 'd', 'e']
print(t)

# index
# 3
print(t.index('d'))

# pop
# e
print(t.pop())
# ['a', 'b', 'c', 'd']
print(t)

a = ['x', 'y', 'z']

# extend
t.extend(a)
# ['a', 'b', 'c', 'd', 'x', 'y', 'z']
print(t)