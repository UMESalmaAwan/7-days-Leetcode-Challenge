class Solution(object):
    def canJump(self, nums):
        max_reachable_index = 0
        
        # Iterate through the array
        for i, jump_length in enumerate(nums):
            # Check if the current index is beyond the maximum reachable index
            if i > max_reachable_index:
                return False
            
            # Update the maximum reachable index based on the current jump length
            max_reachable_index = max(max_reachable_index, i + jump_length)
            
            # If the maximum reachable index reaches or exceeds the last index, return True
            if max_reachable_index >= len(nums) - 1:
                return True
        
        # If the loop completes without returning, it means the last index cannot be reached
        return False

# Example usage:
solution = Solution()
nums = [2, 3, 1, 1, 4]
print(solution.canJump(nums))  # Output: True

        