class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b=bin(N)
        has=0
        dis=[]
        comput=[]
        for num in b:
            if num == '1':
                has = has+1
        if has <= 1:
            return 0
        else:
            obj=str(b)
            for i in range(len(obj)):
                if obj[i]=='1':
                    dis.append(i)
            for j in range(len(dis)-1):
                comput.append(dis[j+1]-dis[j])
            return max(comput)
            
