#26.06.25
num = int(input())
count = 0
hi = 100
lo = 0
while True:
    mid = (lo+hi)//2
    count += 1
    if num == mid:
        break
    elif num < mid:
        hi = mid-1
    elif num > mid:
        lo = mid+1
print(count-1)
#2/10 Partial Score