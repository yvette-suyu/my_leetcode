1. xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。


>>>xrange(8)
xrange(8)
>>> list(xrange(8))
[0, 1, 2, 3, 4, 5, 6, 7]
>>> range(8)                 # range 使用
[0, 1, 2, 3, 4, 5, 6, 7]



2. map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。map(function, iterable, ...)


>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]