#19.06.25
age = int(input())
char = input()

for i in range(len(str(age))+2):        #iterating through 2 + number of digits to work out number of characters needed
    if i != len(str(age))+1:
        print(char, end="")     #ending with no space to print the characters all together
    else:
        print(char, end= "\n")      #printing the characters, then starting a new line to allow for next string of characters

print(char + str(age) + char, end="\n")         #adding characters and digits into the badge

for i in range(len(str(age))+2):        #ending the badge with a line of characters again
    print(char, end="")
#3/3 Full Score 
