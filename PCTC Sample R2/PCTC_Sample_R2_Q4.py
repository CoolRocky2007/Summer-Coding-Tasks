#24.06.25
x = str(input())
y= int(input())

x = x[::-1]
string = ""

for i in range(y):
    string += x
print(string)