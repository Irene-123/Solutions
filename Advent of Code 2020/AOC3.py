file=open('/home/kirti/Downloads/input.txt','r')
contents=file.read()
contents=list(contents.split('\n'))[:-1]
n=len(contents)

lst=[]
for content in contents:
   content=n*content
   lst.append(list(content))
print(lst)
count=0

i=1
j=3
while i < len(lst) and j < len(lst[0]):
    if lst[i][j]=='#':
        count+=1
    j+=3
    i+=1




print(count)
