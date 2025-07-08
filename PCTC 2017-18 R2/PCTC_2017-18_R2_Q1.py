#07.07.25
x = int(input())
y = int(input())
z = int(input())

if x > y:
    if x-y == z:
        print("HAPPY CROWD")
    elif x+y == z:
        print("HAPPY CROWD")
    else:
        print("UNHAPPY CROWD")
elif y > x:
    if y-x == z:
        print("HAPPY CROWD")
    elif y+x == z:
        print("HAPPY CROWD")
    else:
        print("UNHAPPY CROWD")
else:
    print("UNHAPPY CROWD")
#9/10 Partial Score