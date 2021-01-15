def oddeven(arr,n):
    diff=0
    ans=0
    pos=[0]*(n+1)
    neg=[0]*(n+1)
    pos[0]=1
    for i in range(n):
        if arr[i] & 1==1:
            diff+=1
        else:
            diff-=1
        if diff<0:
            ans+=neg[-diff]
            neg[-diff]+=1
        else:
            ans+=pos[diff]
            pos[diff]+=1
    return ans
 
n= int (input())
arr=list(map(int,input().split()))
o=oddeven(arr,n)
print(o)
