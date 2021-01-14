file=open('/home/kirti/Downloads/input.txt','r')
contents=file.read()
seats=list(contents.split('\n'))[:-1]


def binary1(seat):
    left,right=0,127
    i=0
    while left < right and i < 7:
        mid=(left+right)//2
        if seat[i]=='F':
            right=mid
        else:
            left=mid+1
        i+=1
    print('First',mid)
    return mid


def binary2(seat):
    left,right=0,7
    i=7
    while left < right and i < 10:
        mid=(left+right)//2
        if seat[i]=='L':
            right=mid
        else:
            left=mid+1
        i+=1
    print('second',mid)
    return left



res=0
for seat in seats:
    first=binary1(seat)
    second=binary2(seat)
    c=first*8 + second
    res=max(res,c)
print(res)
