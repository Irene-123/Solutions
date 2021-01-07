
            


file=open('/home/kirti/input.txt','r')
contents=file.read()
nums=list(map(int,contents.strip().split('\n')))
file.close()

numset=set(nums)
for i in range(len(nums)):
    a=nums[i]
    for j in range(i+1,len(nums)):
        b=nums[j]
        c=2020-a-b
        if c in numset:
            print(a*b*c)
            break


    




                  

