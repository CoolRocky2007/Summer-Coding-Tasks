#19.06.25
age = int(input())
char = input()

for i in range(len(str(age))+2):
    if i != len(str(age))+1:
        print(char, end="")
    else:
        print(char, end= "\n")

print(char + str(age) + char, end="\n")

for i in range(len(str(age))+2):
    print(char, end="")
#3/3 Full Score 