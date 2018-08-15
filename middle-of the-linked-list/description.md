之前做过关于链表的的问题，判断是否为有环链表。
链表，如其英文名：linked-list，是指在存储中是有连接的，所以在使用中可以 self.head, self.val, self.next, self.next.next 这样使用。

需要注意的是，它不像一般的list这样，可以直接使用len()求其长度，而是需要自定义。


求链表长度：


```python
    def len(self):         
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        return length
```
