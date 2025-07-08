#06.07.25
shake = str(input())
table = {}

for i in range(len(shake)):
    if shake[i] in table:
        table[shake[i]] += 1
    else:
        table[shake[i]] = 1

for ingredient in table:
    if table[ingredient] < 2 and ingredient == "I":
        print("I")
    elif table[ingredient] < 1 and ingredient == "M":
        print("M")
    elif table[ingredient] < 3 and ingredient == "C":
        print("C")
    elif table[ingredient] < 1 and ingredient == "W":
        print("W")
#4/5 Partial Score