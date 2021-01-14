import re
file=open('/home/kirti/Downloads/input.txt','r')
lines=file.read()

lines=list(lines.strip().split('\n\n'))
#print(lines)
res=[]
for sub in lines:
    res.append(re.sub('\n', '', sub))
print(res)
ans=0
for line in res:
    ans+=len(set(line))
print(ans)
