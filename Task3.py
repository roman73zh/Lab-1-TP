Count = int(input())
data = []
for i in range(Count):
    data.append(input())
Count = int(input())
req = []
for i in range(Count):
    req.append(input())
for i in data:
    flag = 1
    for j in req:
        if j not in i:
            flag = 0
            break
    if flag:
        print(i)