#27.06.25
word = str(input())

while word!= word[::-1]:
    for i in range(len(word)):
        temp = word[:i] + word[i+1:]
    if temp == temp[::-1]:
        word = temp
        break
    else:
        word = word[1:]
print(word)
#6/10 Partial Score