class Node:
	def __init__(self, data, next_node):
		self.data = data
		self.next_node = next_node

class Node_factory:
	def __init__(self, *args):
		if(len(args)==1):
			n = Node(args[1],None)
			self.head=n
		else:
			self.head=None
	
	def insertNode(self, data):
		if (self.head==None): 
			self.head = Node(data,None)
			return self.head
		else:
			head = self.head
			while(head.next_node!=None):
				head = head.next_node
			head.next_node = Node(data, None)


	def reverseLL(node):
	    tail = None
	    head = node
	    
	    while(head!=None):
	        temp = head.next
	        head.next = tail
	        tail = head
	        head = temp
	    return tail
	    
	def reverseLL(n, last=None):
	    if n is None:
	        return last
	    nxt = n.next
	    n.next = last
	    return reverseLL(nxt, n)
