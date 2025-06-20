#20.06.25
num = int(input())      #initial input
total = 0       #intialisation of variables
count = 1
over_100 = 0
while num >= 0 and num < 1000000 and count <= 100:      #conditional testing if input is valid
    if num > 100:       #checking if num is part of over_100 or not
        over_100+=1
    total += num        #out of the if statement
    num = int(input())
    count += 1
print(total)
print(over_100)     #printing amount of numbers inputted over 100
#3/3 Full Score