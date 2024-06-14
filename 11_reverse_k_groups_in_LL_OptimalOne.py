 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head
        mainHead, tail = None, None 
        length = 0 
        curr = head 
        while curr:
            curr = curr.next 
            length += 1 
        
        if length < k:
            return head
        curr = head
        while length >= k and curr:
            temp = curr 
            prev = None
            for i in range(k):
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
            
            if mainHead == None:
                mainHead = prev 
                tail = temp 
            else:
                tail.next = prev 
                tail = temp 
            length -= k
        tail.next = curr 
        return mainHead
        
