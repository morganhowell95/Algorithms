'''

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
Show Tags
Show Similar Problems
'''
class Solution(object):
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        #convert board to a connected map
        map = {};
        
        for i in range(len(board)):
            board[i]= list(board[i][0])
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                map[(i,j)] = set()
                #checking coordinates around cell
                up = i-1
                down = i+1
                left = j-1
                right = j+1
                #add coordinate as connected if within bounds
                if(down<len(board)):
                    map[(i,j)].add((down,j))
                    
                if(up>=0):
                    map[(i,j)].add((up,j))
                    
                if(left>=0):
                    map[(i,j)].add((i,left))
                    
                if(right<len(board[i])):
                    map[(i,j)].add((i,right))
                    
                    
        self.map = map
        self.board = board
        self.word = word
        self.word_found=False
            
        #follow word within map using variance of greedy algorithm
        success=False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == word[0]):
                    success = self.follow_word(map, (i,j))
                    if(success or len(word)==1 or len(word)==0): 
                        success=True
                        self.word_found=True
                    else:
                        self.word_found=False
        return success
    
    
    def follow_word(self, graph, start, visited=None, wordcount=1):
        if visited is None:
            visited = set()
                    
        visited.add(start)
        for next in graph[start] - visited:
            y = next[0]
            x = next[1]
            if(wordcount < len(self.word) and self.board[y][x] == self.word[wordcount]):
                if wordcount==len(self.word)-1:
                    self.word_found= True
                self.follow_word(graph, next, visited, wordcount+1)
            
        return self.word_found
        