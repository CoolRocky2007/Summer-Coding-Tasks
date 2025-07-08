#08.07.25
reps = int(input())
yes = 0
no = 0

for i in range(reps):
    vote = str(input())
    if vote == "YES":
        yes += 1
    elif vote == "NO":
        no += 1
print("YES", yes)
print("NO", no)
#10/10 Full Score