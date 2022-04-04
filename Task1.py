offset = int(input())
text = input()
for i in text:
    if 1072 <= ord(i) <= 1103 and offset % 32 != 0:
        if ord(i) + offset > 1103:
            print(chr(ord(i) - 32 + offset % 32), end="")
        else:
            print(chr(ord(i) + offset), end="")
    elif 1040 <= ord(i) <= 1071 and offset % 32 != 0:
        if ord(i) + offset > 1071:
            print(chr(ord(i) - 32 + offset % 32), end="")
        else:
            print(chr(ord(i) + offset), end="")
    else:
        print(i, end="")