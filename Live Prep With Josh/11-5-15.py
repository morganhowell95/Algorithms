
class LinkedList:
    
    def __init__(self, ll=None):
        self.root = ll 
        self.tail = ll
        
    def insert(self, data):
        if not self.root: 
            self.root = LinkedList.Node(data)
            self.tail = self.root
        else: 
            self._insert(data)
    
    def _insert(self, data):
        self.tail.next = LinkedList.Node(data)
        self.tail = self.tail.next
        
    def getList(self):
        return self.root
    
    #node class
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

#creating a linked list
ll = LinkedList()
for i in range(0,10):
    ll.insert(i)
head = ll.getList()



#reverse link list recursively
def rreverseLL(root, prev=None):
    if not root == None:
        temp = root.next
        root.next = prev
        return rreverseLL(temp, root)
    else:
        return prev
    
#reverse link list recursively
def ireverseLL(root):
    prev = None
    curr = root
    while curr!=None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

#interweave nodes of a linked list
def interweave(root):
    i = root
    j = root
    
    #put slower runner i in the middle of the linked list
    while(j!=None and j.next!=None):
        i = i.next
        j = j.next
        if (j.next != None):
            j=j.next
            
    #start interleaving nodes
    head = root
    mid = i
    while(mid!=None):
        temp1 = head.next
        temp2 = mid.next
        head.next = mid
        mid.next = temp1
        mid = temp2
        head = temp1
    
    return root
        
head = interweave(head)
for i in range(0,10):
    print head.data
    head = head.next
            
#compute numbers within array multiplied by the depth
def computeDepths(arr, level=1):
    final = 0
    for i in arr:
        if type(i) is list:
            final += computeDepths(i, level+1)
        else:
            final += (i*level)
    return final

print '------------------'
a = [1,2,[3,1,4,[1,6]]]

print computeDepths(a)

#flatten array
def flattenArray(arr):
    result = []
    for el in arr:
        if type(el) is list:
            result.extend(flattenArray(el))
        else:
            result.append(el)
    return result

print '------------------'
a = [1,2,[3,1,4,[1,6,8,8]]]

print flattenArray(a)


#given M sorted arrays with N elements
def mergeArrays(arr):
    if len(arr)>1:
        next_gen = []
        for i in xrange(0,len(arr)-1,2):
            curr = arr[i]
            next = arr[i+1]
            merged_array = []
            #index counts for left and right subarrays, as well as arr
            k=0
            w=0
            
            #merging two subarrays into one array
            while k<len(curr) and w<len(next):
                if(curr[k] <= next[w]):
                    merged_array.append(curr[k])
                    k+=1
                else:
                    merged_array.append(next[w])
                    w+=1
                    
            while k<len(curr):
                    merged_array.append(curr[k])
                    k+=1
                    
            while w<len(next):
                    merged_array.append(next[w])
                    w+=1
                    
            next_gen.append(merged_array)
        arr = mergeArrays(next_gen)           
    else:
        arr = arr[0] if arr else None

    return arr





'''
MY IMPLEMENTATION OF LONGEST SUBSEQUENCE
'''

#my solution is to create a BST a label nodes with number of inserts to the right of that node
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bst = Solution.BST()
        for i in nums:
            bst.insert(i)
            
        return bst.fetchLargestSubArrayLength()
             
    class Node(object):
        lc = None
        rc = None
        seq = 1
        def __init__(self, num):
            self.num = num
            
    class BST(object):
        max_sublength = 1
        
        def __init__(self, root=None):
            if(root):
                self.root = root
            else:
                self.root = None
                
        def fetchLargestSubArrayLength(self):
            return self.max_sublength
                
        def insert(self, num):
            if(self.root==None):
                self.root = Solution.Node(num)
            else:
                self._insert(num)
                
        def _insert(self, num):
            head = self.root 
            
            while(head != None):
                if(num<=head.num):
                    if(head.lc==None):
                        head.lc = Solution.Node(num)
                        head = None
                    else:
                        head = head.lc
                else:
                    head.seq = head.seq+1
                    if(head.seq>self.max_sublength): self.max_sublength = head.seq
                    if(head.rc==None):
                        head.rc = Solution.Node(num)
                        head = None
                    else:
                        head = head.rc  
      

        def _insertR(self, num, node=None):
            if(not node): node = self.root
        
            if(node.num>=num):
                if(node.lc == None):
                    node.lc = Solution.Node(num)
                else:
                    self._insert(num, node.lc)
                    
            if(node.num<num):
                node.seq = node.seq+1
                if(node.rc == None):
                    node.rc = Solution.Node(num)
                else:
                    if(node.seq>self.max_sublength): self.max_sublength = node.seq
                    self._insert(num, node.rc)
