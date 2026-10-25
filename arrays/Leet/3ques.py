

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0

        while len(str(num)) > 1:
            sum = 0
            while num:
                sum += num % 10
                num = num // 10
            num = sum

        return num



class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        while n:
            if n==0:
                return False
            elif n<0:
                return False
            else:
                if n==1:
                    return True
            if n%2!=0:
                return False
                break
            n=n//2
        return True

        

class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        c=(bin(a+b))
        return c[2:]
        