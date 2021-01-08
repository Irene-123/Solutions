
file=open('/home/kirti/Downloads/input.txt','r')
contents=file.read()
grid=list(contents.split('\n'))[:-1]
height = len(grid)
width = len(grid[0])

def count(i,j):
    x,y,count=0,0,0
    while y < height:
        if grid[y][x%width]=='#':
            count+=1
        x+=i
        y+=j
    print(count)
    return count

ans=1
for d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    ans*=count(*d)
print(ans)
