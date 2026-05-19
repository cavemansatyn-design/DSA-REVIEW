class Solution(object):
    def maxProfit(self, prices):
        curr=0
        mini=prices[0]
        for t in range(len(prices)):
            mini=min(prices[t],mini)
            curr=max(prices[t]-mini,curr)
        return curr
            

        