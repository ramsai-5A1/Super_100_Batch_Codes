class ListNode:
	def __init__(self, val):
		self.val = val
		self.prev = None 
		self.next = None 
		

class DoublyLinkedList:
	def __init__(self):
		self.head = None 
		self.tail = None 
		
		
	def addNodeAtTailPosition(self, data):
		newNode = ListNode(data)
		if self.head == None:
			self.head = self.tail = newNode 
			return 
		
		self.tail.next = newNode 
		newNode.prev = self.tail 
		self.tail = newNode 
		
		
	def printDLLFromLeftToRight(self):
		print("Left to Right: ")
		currNode = self.head 
		while currNode:
			print(currNode.val, end = " --> ")
			currNode = currNode.next 
		print()
			
	def printDLLFromRightToLeft(self):
		print("Right to Left:")
		currNode = self.tail 
		while currNode:
			print(currNode.val, end = " --> ")
			currNode = currNode.prev 
		print()
		
	def reverseKGroupsInDLL(self, k):
		currNode = self.head 
		length = 0 
		while currNode:
			currNode = currNode.next 
			length += 1 
			
		if length < k:
			return 
		
		currNode = self.head
		currMainHead, currTail = None, None
		while length >= k:
			temp = currNode
			previousNode = None
			for i in range(k):
				nextNode = currNode.next 
				currNode.next = previousNode
				if previousNode:
					previousNode.prev = currNode
				previousNode = currNode
				currNode = nextNode
			if currMainHead == None:
				currMainHead = previousNode 
				currMainHead.prev = None
				currTail = temp 
			else:
				currTail.next = previousNode 
				previousNode.prev = currTail
				currTail = temp
				
			length -= k 
		if currNode:
			currTail.next = currNode
			currNode.prev = currTail
			
		self.head = currMainHead
		while currTail.next:
			currTail = currTail.next 
			
		self.tail = currTail
			
			
			
list1 = DoublyLinkedList()
list1.addNodeAtTailPosition(10)
list1.addNodeAtTailPosition(20)
list1.addNodeAtTailPosition(30)
list1.addNodeAtTailPosition(40)
list1.addNodeAtTailPosition(50)
list1.addNodeAtTailPosition(60)
list1.addNodeAtTailPosition(70)
list1.addNodeAtTailPosition(80)
list1.addNodeAtTailPosition(90)
list1.addNodeAtTailPosition(100)

list1.printDLLFromLeftToRight()
list1.printDLLFromRightToLeft()

list1.reverseKGroupsInDLL(3)

list1.printDLLFromLeftToRight()
list1.printDLLFromRightToLeft()
