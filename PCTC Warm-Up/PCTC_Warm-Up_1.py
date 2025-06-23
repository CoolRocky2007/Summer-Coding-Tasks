#19.06.25
amount_list = []        #initialising list
total = 0
for i in range(5):      #iterating 5 times
    amount = int(input())
    amount_list.append(amount)      #appending amount to list
    total += amount     #calculating total amount
index = int(input())
print('$' + str(total - amount_list[index-1]))      #printing the amount left after subtracting amount given from index
#3/3 Full Score
