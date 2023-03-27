import sys
import re

from pathlib import Path
Link = sys.argv[1]
Link=Path(Link)
Files = open(Link)
Massiv = []
for i in Files:
    if re.search(r'\d' ,i) != None:
        Massiv.append(int(i))
    else:
        print('Ошибка в строке. Значение != Цифре')
        quit()
count = 0
SredZnach = 0
for i in Massiv:
    SredZnach = i+SredZnach
SredZnach = SredZnach/len(Massiv)
SredZnach = SredZnach.__floor__()

while True:
    for i in Massiv:
        ind = Massiv.index(i)
        if i < SredZnach:
            Massiv[ind] = i+1
            count = count+1
        elif i > SredZnach:
            Massiv[ind] = i - 1
            count = count + 1
        elif i == SredZnach:
            continue
        if len(set(Massiv)) == 1:
            break
    if len(set(Massiv)) == 1:
        break
print(count)
