sum1 = 0
bigger = 0
smaller = 1000
list1 = [8, 1000, -3, 2, 5]
lenght = len(list1)
for i in list1:
    sum1 = sum1 + i
    if i >= bigger:
        bigger = i
    if i <= smaller:
        smaller = i
print('the list sum: ',sum1)
print('biggest numbers is: ', bigger)
print('smallest number is: ', smaller)
print('the average of the list values is: ', sum1 / lenght)
list2 = [8, 1000, -3, 2, 5]
lenghthalf = len(list2) // 2
list2.remove(lenghthalf)
print('the list without the middle value: ', list2)
# יש לי בעייה עם סוף התרגיל, מקווה שאיתי יוכל לסגור לי את הפינה, כי אני לא מצליח להוציא משום מה את האמצעי
# מתוך הרשימה ע"י פונקציית len. זה מוציא לי את האינדקס הלא נכון