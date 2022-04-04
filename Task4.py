str = list(input())
prevChar = str[0]
charCount = 1
while len(str) > 1:
    str.pop(0)
    if not str[0] == prevChar:
        print(charCount, prevChar)
        charCount = 0
    prevChar = str[0]
    charCount += 1
print(charCount, prevChar)