class node:
    left_child = None
    right_child = None
    data = None
    def __init__(self, data, lc, rc):
        self.data = data
        self.left_child = lc
        self.right_child = rc


class bst:
    root = None

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        current_node = self.root

        if current_node is None: 
            self.root = node(data, None, None)
            return self.root

        while(current_node!=None):
            if data>=current_node.data: 
                if(not current_node.right_child):
                    current_node.right_child = node(data, None, None)
                    current_node = None
                else:
                    current_node = current_node.right_child
            else:
                if(not current_node.left_child):
                    current_node.left_child = node(data, None, None)
                    current_node = None
                else:
                    current_node = current_node.left_child
                    
    def printinorder(self, root):
        if(root.left_child!=None):
            self.printinorder(root.left_child)
            
        print root.data
        
        if(root.right_child!=None):
            self.printinorder(root.right_child)
        

bs = bst()
sum = 0
for i in range(0,10):
    bs.insert(i)
    sum = sum + i
print "sum: " + str(sum)
root = bs.root

bs.printinorder(root)
print '-----------------------'
#sum all data
def sum_data(root):
    if(root==None): return 0
    else: 
        return sum_data(root.left_child) + sum_data(root.right_child) + root.data

#max height

def max_height(root):
    if(root==None): return 0
    else: return max(max_height(root.left_child), max_height(root.right_child)) + 1
    
def max(a, b):
    if a>b:
        return a
    else:
        return b

#count leaves
def count_leaves(root):
    if(root is None):
        return 0
    if(root.left_child is None and root.right_child is None):
        return 1
    return count_leaves(root.left_child) + count_leaves(root.right_child)

print count_leaves(root)
