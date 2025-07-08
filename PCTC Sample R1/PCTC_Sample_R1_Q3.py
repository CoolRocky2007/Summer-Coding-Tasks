#05.07.25
word = str(input())
count = 1
output = word
while count*len(word) < 30:
    count += 1
    output += word
print(output)
#2/3 Partial Score