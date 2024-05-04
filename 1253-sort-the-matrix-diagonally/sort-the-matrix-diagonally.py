class Solution(object):
    def diagonalSort(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = {}

        # Store the elements of each diagonal in a dictionary
        for i in range(m):
            for j in range(n):
                if i - j not in diagonals:
                    diagonals[i - j] = []
                diagonals[i - j].append(mat[i][j])

        # Sort the elements of each diagonal separately
        for key in diagonals:
            diagonals[key].sort()

        # Update the matrix with sorted elements
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop(0)

        return mat
