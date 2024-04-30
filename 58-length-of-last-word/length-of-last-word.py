class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        words = s.split(' ')
        # Return the length of the last word
        return len(words[-1]) if words else 0

# Create an instance of the Solution class
solution = Solution()

# Call the length_of_last_word method with the input string 's'
s = "Hello world"
#s = "fly me   to   the moon "
# s = "luffy is still joyboy"
ret = solution.lengthOfLastWord(s)
print(ret)
print("The last word is 'world' with length", ret)