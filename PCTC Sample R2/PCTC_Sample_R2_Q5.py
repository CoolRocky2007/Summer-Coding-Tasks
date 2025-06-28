#27.06.25
n = int(input())
now = "1"

for i in range(n):
    next = ""
    j = 0
    while j < len(now):
        count = 1
        while j+1 < len(now) and now[j] == now[j+1]:
            count += 1
            j += 1
        next += str(count) + now[j]
        j += 1
    now = next
print(now)
#10/10 Full Score