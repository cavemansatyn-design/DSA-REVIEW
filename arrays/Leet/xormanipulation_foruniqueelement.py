class Solution(object):
    def singleNumber(self, nums):
        op=0
        for t in nums:
            op^=t
        return op

        
        