#29.06.25
deck = str(input())
deck_value = 0
hand_value = 0

index = (int(input())*2)-1
result = ""

for i in range(len(deck)):
    hand_count = 0
    if i >= index and hand_value < 21:
        if deck[i] == "A":
            hand_value += 11
            hand_count += 1
        elif deck[i].upper() == "T" or deck[i].upper() == "J" or deck[i].upper() == "K" or deck[i].upper() == "Q":
            hand_value += 10
            hand_count += 1
        elif int(deck[i]) <= 1:
            print("invalid deck")
        else:
            hand_value += int(deck[i])
            hand_count += 1

if hand_value == 21:
    result = "A"
elif hand_value > 21:
    result = "D"
elif hand_value < 21 and hand_count < 5:
    result = "C" + str(hand_value)
elif hand_value < 21 and hand_count == 5:
    result = "B"

print(result)



