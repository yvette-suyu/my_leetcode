class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        num = len(str(x))
        if num % 2 == 0:
            x = str(x)
            for i in range(num/2):
                if x[i] == x[num-1-i]:
                    print("ok")
                else:
                    return False
            return True
        else:
            mid = (num-1)/2 
            x = str(x)
            for j in range(mid+1):
                if x[mid-j] == x[mid+j]:
                    print("ok")
                else:
                    return False
            return True
