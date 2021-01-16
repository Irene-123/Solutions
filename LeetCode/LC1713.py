class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dic={num:i for i,num in enumerate(target)}
        A=[]
        for num in arr:
            if num in dic:
                A.append(dic[num])
        return len(target)-self.lenofLIS(A)   
    def lenofLIS(self,nums):
        if not nums:
            return 0
        piles=[]
        for num in nums:
            index=bisect.bisect_left(piles,num)
            if index==len(piles):
                piles.append(num)
            else:
                piles[index]=num
              
        return len(piles)       
             
