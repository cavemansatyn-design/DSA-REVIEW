class Solution(object):
    def maxArea(self, height):
        mvol=0
        vol=0
        l=0
        r=len(height)-1
        while l<=r:
            width=r-l
            heighta=min(height[l],height[r])
            vol=width*heighta
            mvol=max(mvol,vol)
            if height[l]<height[r]:
                l=l+1

            else:
                
                r=r-1
            
        
        return mvol
            