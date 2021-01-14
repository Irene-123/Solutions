from collections import Counter
file=open('/home/kirti/Downloads/input.txt','r')
lines=file.read()

lines=list(lines.strip().split('\n\n'))
res=[]
for line in lines:
    l=[line.split('\n')]
    res.append(l)
print(res)
ans=0

print(sum(len(y[0]) if len(y) == 1 else len(set(y[0]).intersection(*y[1:])) for line in res for y in line))
