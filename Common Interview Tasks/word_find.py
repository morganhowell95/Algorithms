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
                    map[(i,j)].add(down,j)
                    
                if(up>=0):
                    map[(i,j)].add(up,j)
                    
                if(left>=0):
                    map[(i,j)].add(i,left)
                    
                if(right<len(board[i]))
                    map[(i,j)].add(down,right)
        
        #follow word within map using variance of greedy algorithm
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == word[0]):
                    success = follow_word(map, (i,j), word, board)
                    if(success): return True
                    
        return False
        
        
    #implementing DFS to follow a word from start vertex
    def follow_word(map, start, word, board):
        (visited, stack) = (set(),[start])
        word_found = false
        letter_count = 0;
        
        while(stack):
            node = stack.pop()
            letter_count = letter_count+1
            if node is not in visited:
                visited.add(node)
                
                #don't look through nodes that do not contain the next letter
                for tuple in (map[node]-visited):
                    if(board[tuple[0]][tuple[1]] != word[letter_count]):
                        visited.add(tuple)
                        
                stack.extend(map[node]-visited)
                
                
        return visited
        