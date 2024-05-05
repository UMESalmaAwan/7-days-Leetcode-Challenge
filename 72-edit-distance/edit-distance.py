class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        # Initialize  table with dimensions (m+1) x (n+1)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    table[i][j] = j
                elif j == 0:
                    table[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1])
        
        return table[m][n]

        