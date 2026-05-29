class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        else:
            for k in range(32):
                if pow(3,k)==n:
                    return True
            return False
        