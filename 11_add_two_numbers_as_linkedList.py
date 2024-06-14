# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = None
        tail = None

        while carry > 0 or l1 != None or l2 != None:
            value = carry
            if l1 != None:
                value += l1.val
                l1 = l1.next
            if l2 != None:
                value += l2.val
                l2 = l2.next
            
            currNode = ListNode(value % 10)
            carry = value // 10 
            if head == None:
                head = currNode
                tail = currNode
            else:
                tail.next = currNode
                tail = tail.next

        return head
