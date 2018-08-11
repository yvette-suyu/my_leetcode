class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        if bills[0]!=5:
            return False
        if bills[0]==5:
            for i in range(len(bills)):
                if bills[i]==5:
                    five=five+1
                if bills[i]==10:
                    ten=ten+1
                    five=five-1
                    if five<0:
                        return False
                if bills[i]==20:
                    if ten>0 :
                        ten=ten-1
                        five=five-1
                    else:
                        five=five-3
                    if ten<0 or five<0:
                        return False
            return True
                    
                    
