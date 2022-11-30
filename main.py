import random
import time
import os
from msvcrt import getch

with open("keywords.txt", encoding="utf-8") as file:
    data = file.read().splitlines()


wordArray = []
ort = 0
y = 0
while ort < 4.8 or ort > 5.2:
    ort = 0
    wordArray = []
    y = 0
    for x in range(0, 60):
        wordArray.append(random.choice(data))
    for x in wordArray:
        y += len(x)

    ort = y/60
    print(ort)
string = ""
testArray = []
point = 0
second = 30
timer = time.time()
unicodeDict = {
    159: "\u015F",
    141: "\u0131",
    135: "\u00E7",
    167: "\u011F",
    129: "\u00FC",
    148: "\u00F6"
}
hexDict = {
    "\x9f": "ş",
    "\x87": "ç",
    "\xa7": "ğ",
    "\x8d": "ı",
    "\x81": "ü",
    "\x94": "ö"
}
os.system('cls')
for x in wordArray:
    print(x, end=" ")
print("\n\n")
getch()
print("-------------------")
print("\n")
while True:
    if time.time() - timer > second:
        break

    key = ord(getch())
    try:
        print(unicodeDict[key], end="")
    except:
        print(chr(key), end="")

    if key == 32:
        testArray.append(string)
        string = ""
    elif chr(key) == "q":
        print(testArray)
        break
    else:
        if key == 8:
            string = string[:-1]
        else:
            try:
                key = hexDict[chr(key)]
            except:
                key = chr(key)
            string += key
for x, y in zip(wordArray, testArray):
    if x == y:
        point += len(x) + 1

wpm = (point / 5) * (60 / second)

print("\n\n")
print(f"Toplam doğru vuruş sayısı = {point}")
print(f"Dakika başına kelime = {int(wpm)}")
