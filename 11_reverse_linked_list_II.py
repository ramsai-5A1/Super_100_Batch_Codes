# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummyHead = ListNode(-1)
        dummyHead.next = head
        tail = dummyHead

        currHead = head 
        position = 1 
        previousNode = dummyHead

        while position < left:
            previousNode = currHead
            currHead = currHead.next 
            position += 1

        prev = None
        tail = currHead
        while position <= right:
            next = currHead.next 
            currHead.next = prev 
            prev = currHead 
            currHead = next 
            position += 1 

        previousNode.next = prev 
        tail.next = currHead
        
        return dummyHead.next
