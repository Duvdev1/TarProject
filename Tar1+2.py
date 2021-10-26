#targil1: if the split is not done by 'space' it could be done by any other string
# or number that also counted as a string

#2:

string1 = input('insert a sum question and the answer')
list1 = string1.split("=")
answer = list1[1]
answer = float(answer)
sumToString = list1[0]
list2 = sumToString.split("+")
sum1= 0
for i in list2:
    i = float(i)
    sum1 = sum1 + i
if sum1 == answer:
    print("True")
else:
    print("false")


