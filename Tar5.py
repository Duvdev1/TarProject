list1 = ['help' , 'pie', 'pen', 'world of coding']
for i in range(len(list1)):
    s = list1[i]
    if len(s) <= 4:
        upper1 = s.upper()
        print(upper1)
    else:
        break