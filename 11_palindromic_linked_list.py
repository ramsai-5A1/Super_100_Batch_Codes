# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doReverse(self, head):
        current = head
        previous = None

        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        
        slow, fast = head, head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head1 = head

        head2 = self.doReverse(head2)
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True
