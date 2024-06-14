# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2 
        elif list2 == None:
            return list1 
        
        dummyNode = ListNode(-1)
        tail = dummyNode 
        head = dummyNode 

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next 
            else:
                tail.next = list2 
                list2 = list2.next 
            tail = tail.next

        if list1:
            tail.next = list1 
        else:
            tail.next = list2
        return head.next



        
        
