fullname = "Roy Duvdevani"
count1 = 0
for a in range(len(fullname) - 1, len(fullname) - 6, -1):
    print('last five:  ', fullname[a])
for b in range((len(fullname)  // 3)):
    print('the first third of the full name: ', fullname[b])
print("count of letter a is :", fullname.count("a"))
if fullname.count("b") >= 1:
    print("True, contains the letter b")
else:
    print("False, the string does not contain the letter b")
list1 = fullname.split(" ")
print("string to list:  ")
print(list1)
list2 = fullname.split(" ")
list2.reverse()
print('the opposit list: ', list2)
second = list1[1].upper()
print('big letters for family name: ', second)
list3 = fullname.split(" ")
privatename = list3[0]
privatename = privatename.replace(privatename[len(privatename)//2], "")
print('the name without the middle letter will be: ', privatename)
