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
    string=strings[i]
    l=ranges[i][0]
    r=ranges[i][1]
    if (string[l-1]==chars[i])^ (string[r-1]==chars[i]):
        valid+=1
print(valid)
