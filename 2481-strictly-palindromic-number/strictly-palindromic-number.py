class Solution(object):
    def is_palindromic(self, s):
        return s == s[::-1]

    def isStrictlyPalindromic(self, num):
        if num <= 2:
            return True
        
        for base in range(2, num - 1):
            num_str = ""
            a = num
            while a:
                remainder = a % base
                num_str = str(remainder) + num_str
                a //= base
            
            if not self.is_palindromic(num_str):
                return False
        
        return True

# Example usage:
solution = Solution()
n = 121
print(solution.isStrictlyPalindromic(n))
