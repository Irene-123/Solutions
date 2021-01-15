n = int(input())

a = [[] for i in range(100)]
for i in range(n):
    x,s = input().strip().split()
    if i < n//2:
        s = '-'
    a[int(x)].append(s)

for ele in a :
    for l in ele:
       print(l,end=' ')
#print(' '.join([element for sublist in a for element in sublist]))
