class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lenA = len(A)
        lenB = len(B)     
        if A == '' or B == '':
            return False
        if lenA <=0 or lenA >= 20000:
            return False
        if lenB <=0 or lenB >= 20000:
            return False
        # if issame(A) and issame(B):
        #     return True
        if lenA == lenB:
            count = 0
            C=[]

            for i in range(lenA):
                if A[i] != B[i]:
                    count=count+1
                    C.append(i)
                if count==2:
                    temp0=int(C[0])
                    temp1=int(C[1])

                    if A[temp0]==B[temp1] and A[temp1]==B[temp0]:
                        return True
                    else:
                        return False

        if A==B:
            c=set()
            for a in A:
                if a in c:
                    return True  
                c.add(a)       
            return False
                      

        else:
            return False
        
                
                    
