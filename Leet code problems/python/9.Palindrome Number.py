class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l=0
        if x>0:
            c=x
            while(c>0):
                l=l+1
                c=c//10
            i=eval("10**(l-1)")
            c=x
            su=0
            while(x>0):
                su=su+(x%10)*i
                x=x//10
                i=i/10
            if su==c:
                return True
            else:
                return False
        elif x==0:
            return True
        else:
            return False

#optimised code

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0 or (x!=0 and x%10==0)):
            return False
        s=0
        while(x>s):
            s=s*10+x%10
            x=x//10
        if(x==sum or x==sum//10):
            return True
        else:
            return False