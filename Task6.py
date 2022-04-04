from operator import itemgetter

lst = []
for i in range(int(input())):
    lst.append(input().split())
    lst[i][1] = int(lst[i][1])
lst = sorted(lst, key=itemgetter(2, 1, 0))
for i in range(int(input())):
    result = ""
    req = input()
    for j in lst:
        if req == j[2]:
            result += j[0] + " " + str(j[1]) + " "
    print(result)