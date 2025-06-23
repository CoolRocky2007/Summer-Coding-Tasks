#23.06.25
word = str(input())
n = int(input())

if len(word) == n:
    print("MATCH")
elif len(word) > n:
    print("MORE")
else:
    print("FEWER")
#10/10 Full Score