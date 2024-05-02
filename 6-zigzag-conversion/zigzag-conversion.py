class Solution(object):
    def convert(self, s, numRows):
        # If numRows is 1 or the string length is less than or equal to numRows, return the original string
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Create a list of strings to store characters for each row
        rows = ['' for _ in range(numRows)]
        
        # Initialize variables for tracking current row and direction of movement
        current_row = 0
        direction = 1  # 1 for downward movement, -1 for upward movement
        
        # Iterate through each character in the string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char
            
            # Update the current row and direction based on zigzag pattern
            current_row += direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
        
        # Join the characters from each row and return the result
        return ''.join(rows)

# Example usage:
solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"
