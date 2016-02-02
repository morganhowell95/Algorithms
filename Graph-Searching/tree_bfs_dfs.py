
        
class BST:
    
    def __init__(self, root=None):
        self.root = root
        
        
    def insert(self, val):
        if self.root == None:
            ins = self.root = BST.Node(val)
        else:
            ins = self._insert(val, self.root)
            
        return bool(ins)
    
    def _insert(self, val, root):
        ins = False
        if val > root.val:
            if root.rc == None:
                root.rc = BST.Node(val)
            else:
                ins = self._insert(val, root.rc)
        else:
            if root.lc == None:
                root.lc = BST.Node(val)
            else:
                ins = self._insert(val, root.lc)
                
        return ins
    
    @staticmethod
    def inorder(root):
        
        if root.lc != None:
            BST.inorder(root.lc)
            
        print root.val
        
        if root.rc != None:
            BST.inorder(root.rc)
            
            
    class Node:
    
        def __init__(self, val):
            self.val = val
            self.lc = None
            self.rc = None
            
            
import random   
bst = BST()
for i in range(7):
    num = random.randint(-100,100)
    print "INSERT: ", num
    bst.insert(num)
    
BST.inorder(bst.root)
print '----------------'


#print layers of BST (BFS)
def bfs(root):
    visited = set()
    processing = []
    #in python .pop(0) treats array as queue
    processing.append(root)
    
    while processing:
        
        #pop node from queue and print
        vertex = processing.pop(0)
        print vertex.val
        
        #iterate through adjacent nodes
        if not vertex.lc is None and not vertex.lc in visited:
            processing.append(vertex.lc)
        if not vertex.rc is None and not vertex.rc in visited:
            processing.append(vertex.rc)
            
        visited.add(vertex)
    return visited

#dfs on BST
def dfs(root):
    visited = set()
    stack = []
    stack.append(root)
    
    while stack:
        vertex = stack.pop()
        print vertex.val
        

        if vertex.rc and not vertex.rc in visited:
            stack.append(vertex.rc)
        if vertex.lc and not vertex.lc in visited:
            stack.append(vertex.lc)
        
        visited.add(vertex)
        
dfs(bst.root)


