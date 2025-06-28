#28.06.25
num = int(input())
rev_num = int(str(num)[::-1])
count = 0

while True:
    rev_num = int(str(num)[::-1])
    num += rev_num
    count += 1
    if str(num) == str(num)[::-1]:
        print(count)
        break
#10/10 Full Score