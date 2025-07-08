#05.07.25
finish = []
pos = 0
for i in range(5):
    word = str(input())
    finish.append(word)
for i in range(5):
    if finish[i] == "Ellie" and i+1 == 3:
        print(str(i+1)+"rd")
    if finish[i] == "Ellie" and i+1 == 1:
        print(str(i+1)+"st")
    if finish[i] == "Ellie" and i+1 == 2:
        print(str(i+1)+"nd")
    if finish[i] == "Ellie" and (i+1 == 4 or i+1 == 5):
        print(str(i+1)+"th")
#5/5 Full Score