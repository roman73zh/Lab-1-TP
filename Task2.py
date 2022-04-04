import re

Gl = "АаЕеЁёИиОоУуЫыЭэЮюЯя]"
regExp = ""
cExp = input()
for i in cExp:
    if i == "0":
        regExp += "[" + Gl
    elif i == "1":
        regExp += "[^" + Gl
    elif i == "?":
        regExp += "."
    else:
        regExp += ".*"
matches = 0
while True:
    text = input()
    if text == "":
        break
    if re.match(regExp, text):
        print(text)
        matches += 1
if matches == 0:
    print("Нет результата")