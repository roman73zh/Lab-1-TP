[print(int(i) ** 2, end=" ") for i in input().split() if not int(i) % 2 == 0 and not int(int(i) ** 2) % 10 == 9]