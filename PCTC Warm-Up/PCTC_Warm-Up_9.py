#22.06.25
word = str(input())        #inputting word

for i in range(len(word)):      #iterating through all values of the string
    if word[i] == 'e' and word[i-1] == 'm':     #checking if the values are 'm' and 'e'
        string = word[i-2] + word[i+1]      #concatenating the sandwiching characters

print(string)       #printing the string
#3/3 Full Score