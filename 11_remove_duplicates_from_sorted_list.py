# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head 

        dummyNode = ListNode(-1)
        tail = dummyNode 
        currNode = head 
        previousValue = -101
        while currNode:
            if currNode.val != previousValue:
                tail.next = currNode 
                tail = tail.next 
                previousValue = currNode.val
            currNode = currNode.next

        tail.next = None
        return dummyNode.next
