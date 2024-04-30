class Solution(object):
    def longestCommonPrefix(self, s):
    
        prefix = s[0]
        for string in s[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
            if not prefix:
                return "" #There is no common prefix among the input strings

        return prefix

# Example usage:
solution = Solution()
#s = ["flower","flow","flight"] #here common prefix is fl that show in result
s=["dog","racecar","car"] # not prefix


result = solution.longestCommonPrefix(s)
print(result)
        