#19.06.25
amount_list = []
total = 0
for i in range(5):
    amount = int(input())
    amount_list.append(amount)
    total += amount
index = int(input())
print('$' + str(total - amount_list[index-1]))
#3/3 Full Score