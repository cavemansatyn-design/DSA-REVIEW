
class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=s.strip()
        s1=s
        s2=""
        for t in s:
            if t.isalnum():
                s2=s2+t


        flag=0
        l=0
        r=len(s2)-1
        while l<r:
            if s2[l]==s2[r]:
                l+=1
                r-=1
                flag=0
            else:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True          