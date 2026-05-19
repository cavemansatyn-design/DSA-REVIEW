class Solution(object):
    def isAnagram(self, s, t):
        g=sorted(s)
        h=sorted(t)

        if g==h:
            return True
        else:
            return False
        