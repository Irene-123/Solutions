n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
maxsum=0


for i in range(k):
    maxsum+=arr[i]
sum_=maxsum    


for i,j in zip(range(k-1,-1,-1),range(n-1,(n-k),-1)):
    sum_+=(arr[j])
    sum_-=arr[i]
    maxsum=max(maxsum,sum_)
    
print(maxsum)    


'''
PROBLEM LINK:

https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/staque-1-e790a29f/description/
'''
