from collections import Counter

file=open('/home/kirti/Downloads/input.txt','r')
contents=file.read()
contents=list(contents.split('\n'))[:-1]
strings=[]

chars=[]
ranges=[]
#print(contents[0].split(' ')[2])


for i in range(len(contents)):
    lst=contents[i].split(' ')
    strings.append(lst[2])
    chars.append(lst[1][0])
    ranges.append(list(map(int,lst[0].split('-'))))
n=len(strings)
valid=0
for i in range(n):
    counts=Counter(strings[i])
    if ranges[i][0] <= counts[chars[i]] <= ranges[i][1]:
        valid+=1
print(valid)
