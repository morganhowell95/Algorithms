'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
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
            
        def inordertraverse(self, root):
            if(root.lc!=None):
                self.inordertraverse(root.lc)
                
            print root.seq
            print '-------'
            
            if(root.rc!=None):
                self.inordertraverse(root.rc)
            
