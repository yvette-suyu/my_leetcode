class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        x=y=di=0
        obstacleset=set(map(tuple,obstacles))
        ans=0
        
        for cmd in commands:
            if cmd==-2:
                di=(di-1)%4
            elif cmd==-1:
                di=(di+1)%4
            else:
                for k in xrange(cmd):
                    if (x+dx[di],y+dy[di]) not in obstacleset:
                        x=x+dx[di]
                        y=y+dy[di]
                        ans=max(ans,x*x+y*y)
        return ans
                        