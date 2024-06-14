class Solution(object):
    def reverseKGroup(self, head, k):

        def findLength(head):
            length = 0 
            while head:
                head = head.next 
                length += 1 
            return length 

        length = findLength(head)
        dummyNode = ListNode()
        tail = dummyNode

        curr = head
        while length >= k:
            temp = curr
            prev = None
            for i in range(k):
                next = curr.next 
                curr.next = prev
                prev = curr 
                curr = next 
            tail.next = prev 
            tail = temp
            length -= k 
        tail.next = curr
        return dummyNode.next
