#25.06.25
greatest = '0'
smallest = '}'
word = str(input())
char_list = word.split()

for i in char_list:
    if ord(i) > ord(greatest):
        greatest = i
    elif ord(i) < ord(smallest):
        smallest = i
print(ord(greatest)-ord(smallest))
#8/10 Partial Score