class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string= ''
        left = -pow(2,31)
        right = pow(2,31)-1
        if x>=left and x<=right :
            if x >=0 :
                num = len(str(x))
                for i in range(num):
                    string += str(x % 10)
                    x =  x // 10
                result = int(string)
                if result>=left and result<=right :
                    return result
                else:
                    return 0
            else:
                x = abs(x)
                num = len(str(x))
                for i in range(num):
                    string += str(x % 10)
                    x =  x // 10
                result = - int(string)
                if result>=left and result<=right :
                    return result
                else:
                    return 0

                
        else:
            print("Input data overflow, please input again.")
