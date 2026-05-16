class Solution(object):
    def majorityElement(self, nums):
        l=len(nums)
        k=l//2
        candidate=None
        count=0
        
        # a=0
        # for t in nums:
        #     count=0
        #     for j in nums:
        #         if j==t:
        #             count+=1
        #     if count>k:
        #         return t

        for i in nums:
            if candidate==None or count==0:
                candidate=i
                count=0
            if i==candidate:
                count+=1
            else:
                count-=1

        return candidate