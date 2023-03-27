import sys
n=int(sys.argv[1])
m=int(sys.argv[2])
Massiv=[]
for i in range(n):
    Massiv.append(i+1)
SummaText=''
Iterator=[]
Outstr=''
while True:
    for i in Massiv:
        SummaText+=str(i)
        if len(SummaText) == m:
            if SummaText in Iterator and len(Iterator) > 0: break
            Iterator.append(SummaText)
            Outstr+=SummaText[0]
            SummaText=str(i)
    if len(SummaText) == m:break
print(Outstr)
