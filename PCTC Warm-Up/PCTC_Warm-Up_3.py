#19.06.25
num = int(input())
if num%8 == 0:      #if num is a multiple of 8 already
    print(num)
elif num%8 <= 4:        #if remainder of num/8 is smaller than or equal to four
    print(num-(num%8))      #finding the closest multiple of 8 lower than num
else:
    print(num+(8-(num%8)))      #finding the closest multiple of 8 bigger than num
#2/3 Partial Score