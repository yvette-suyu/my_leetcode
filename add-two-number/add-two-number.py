# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        Ans = ListNode(0)
        p = l1
        q = l2
        curr = Ans
        add = 0
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            ans = add + x + y
            add = ans /10
            curr.next = ListNode(ans % 10)
            curr = curr.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next
            if add>0:
                curr.next = ListNode(add)
        return Ans.next
                
