n = int(input("Enter number of rows: "))

a = 97

for i in range(1,n+1):
    for j in range(1, i+1):
        print("%c" %(a), end="")
    a +=1
    print()


print(f'{n}'*5,end=' ')
print(f'chloe',end=' ')

# prefixes='JKLMNOPQ'
# suffix='ack'
# for letter in prefixes:
#     if letter in 'OQ'