# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return head 

        dummyNode = ListNode(-1)
        tail = dummyNode 
        currNode = head 
        while currNode:
            if currNode.val != val:
                tail.next = currNode 
                tail = tail.next

            currNode = currNode.next 
        tail.next = None
        return dummyNode.next
