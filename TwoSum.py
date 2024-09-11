"""
Problem Level: Easy
Understanding the problem
Given -> array of integers and a target integer
Return -> Indices of the two numbers such that they add up to target
"""

class Solution(object):
    def twoSum(self, nums:list, target:int) -> list:
        """
        this function takes an array and target and returs the indices of the two numbers that add up to target
        
        Args:
            nums (list): This is the list containing numbers
            target (int): This is the number that we want to find the sum of two numbers in the list
            
        Returns:
            list: This is the list containing the indices of the two numbers that add up to target
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == "__main__":
    nums = [8,4,6,14]
    target = 10
    solution = Solution()
    print(solution.twoSum(nums, target))