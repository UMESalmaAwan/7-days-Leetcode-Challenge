class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
    
        return not stack

# Example usage:
solution = Solution()
#CASE 1:
s1 = "()"
print(solution.isValid(s1))

#CASE 2:
s2 = "()[]{}"
print(solution.isValid(s2))
#CASE 3:
s3 = "(]"
print(solution.isValid(s3))  

        