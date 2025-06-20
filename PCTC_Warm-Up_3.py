#19.06.25
num = int(input())
if num%8 == 0:
    print(num)
elif num%8 <= 4:
    print(num-(num%8))
else:
    print(num+(8-(num%8)))