class Solution(object):
  #  def exist(self, board, word):
        
    def exist(self, board, word):
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            # Check if current cell is out of bounds or doesn't match the word character
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return False
            temp = board[row][col]
            board[row][col] = '#'
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(row + dr, col + dc, index + 1):
                    return True
            board[row][col] = temp
            return False
        
        # Main function
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
        