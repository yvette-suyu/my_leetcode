# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
       
        count = head
        index = length/2-1
        if length != 1:
            for i in range(index):
                count = count.next
            return count.next
            
        else:
            return head
