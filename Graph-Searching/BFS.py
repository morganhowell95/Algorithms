#Inspired by 2nd interview of final rounds for G:
#print out the layers of a BST from root to leaves


#Generate BST manually
class BST:

    def __init__(self, node=None):
        if node:
            self.root = node
        else:
            self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BST.Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data > root.data:
            if root.rc is None:
                root.rc = BST.Node(data)
            else:
                self._insert(root.rc, data)
        else:
            if root.lc is None:
                root.lc = BST.Node(data)
            else:
                self._insert(root.lc, data)

    def findData(self, data, root=None):
        
        if root is None:
            if self.root is None:
                return False
            else:
                root=self.root

        if root.data == data:
            return True

        found = False
        if data > root.data:
            if root.rc is None:
                return False
            else:
                found = self.findData(data, root.rc)

        else:
            if root.lc is None:
                return False
            else:
                found = self.findData(data, root.lc)

        return found    

    def getRoot(self):
        return self.root


    class Node:

        def __init__(self, data):
            self.data = data
            self.lc = None
            self.rc = None



#Generate Queue manually using linked list implementation
class LLQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None and self.tail is None:
            node = LLQueue.Node(data)
            self.head = node
            self.tail = node
        else:
            self.tail.ahead = LLQueue.Node(data)
            self.tail = self.tail.ahead

    def dequeue(self):
        if self.head is None:
            return None
        else:
            fetched = self.head.data
            self.head = self.head.ahead
            if self.head is None:
                self.tail = None
            return fetched
        
    def printQ(self):
        start = self.head
        while not start is None:
            print '*', start.data.data
            start=start.ahead

    def isEmpty(self):
        return True if self.head is None else False

    class Node:
        def __init__(self, data):
            self.data = data
            self.ahead = None

class LLFactory:

    def __init__(self, head=None):
        if not head is None:
            self.head = head
        else:
            self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = LLFactory.Node(data)
        else:
            self._insert(data, self.head)

    def _insert(self, data, head):
        last = head
        while not last.ahead is None:
            last = last.ahead
        last.ahead = LLFactory.Node(data)
    

    class Node:
        def __init__(self, data):
            self.data=data
            self.ahead=None
    



#Generatie BFS that prints BST in layers
def printLayersOfBST(root):
    bst_bfs(root, root)
    return True

def bst_bfs(root, start):
    if root is start:
        Q = LLQueue()
        prepare_bfs(root)
        root.dis = 0
        root.color = 'g'
        root.pi = None
    Q.enqueue(root)
    while not Q.isEmpty():
        node = Q.dequeue()
        lc = node.lc  
        rc = node.rc
        print node.data
        print '<->'
        if not lc is None and lc.color == 'w':
            Q.enqueue(lc)
            lc.color = 'g'
            lc.pi = node
            lc.dis = 1 + node.dis
        if not rc is None and rc.color == 'w':
            Q.enqueue(rc)
            rc.color = 'g'
            rc.pi = node
            rc.dis = 1 + node.dis      
        node.color = 'b'

import sys
def prepare_bfs(root):

    if not root.lc is None:
        prepare_bfs(root.lc)

    root.dis = sys.maxint
    root.color = 'w'
    root.pi = None
    
    if not root.rc is None:
        prepare_bfs(root.rc)
        
        
#testing BST insertion
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(100)
tree.insert(6)
tree.insert(101)
tree.insert(5)
tree.insert(4)

def preorderT(root):
    if not root.lc is None:
        preorderT(root.lc)
        
    print root.data
    
    if not root.rc is None:
        preorderT(root.rc)

#Testing Queue functionality 
q = LLQueue()
for i in range(0,10):
    q.enqueue(i)
    
for i in range(0,10):
    print q.dequeue()
    print '->'
    print q.isEmpty()
    
print '*********PRINTING LAYERS OF BST************'

printLayersOfBST(tree.getRoot())
