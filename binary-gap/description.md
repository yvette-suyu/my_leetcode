1.将‘dec’ int input 转换为‘bin’类型

'''
python

  b=bin(N)
'''


然后使用统计1的个数


'''
python
        for num in b:
            if num == '1':
                has = has+1

'''


2.将bin转换为字符串或者是其他类型 用来统计1的位置信息，然后计算连续的1之间的间距。


3.若小于等于一个1，返回0
