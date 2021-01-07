file=open('/home/kirti/input.txt','r')
contents=file.read()
nums=list(map(int,contents.strip().split('\n')))
file.close()
nums.sort()
n=len(nums)
hashes=set(nums[n//2+1:])
for num in nums:
    if 2020-num in hashes:
        print((2020-num)*num)
        break


