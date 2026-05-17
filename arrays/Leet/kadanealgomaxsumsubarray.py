class Solution(object):
    def maxSubArray(self, nums):
        currsum=0
        maxsum=-99999999
        for t in nums:
            currsum+=t
            maxsum=max(maxsum,currsum)
            if currsum<0:
                currsum=0
        return maxsum
        