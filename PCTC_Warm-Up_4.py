#20.06.25
num = int(input())

def func(num):      #recursive function to calculate the number
    if num >= 1000:     #base case, checking if num > 1000
        print(num)
        return num
    else:
        num = (num**2)+1        #calculation
        return func(num)        #function calls itself
func(num)       #calling the function
#3/3 Full Score
