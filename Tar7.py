string1 = 'hello world'
for a in range(0, len(string1)):
    if string1[a] == 'o':
        print('a location in the string', a)
for b in string1:
    print(b, end="")
    if b == 'o':
        break
print()

counto= 0
for b in string1:
    if b == 'o':
        counto += 1
    if counto > 1:
        print(b, end="")





