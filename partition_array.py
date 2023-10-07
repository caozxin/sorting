from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition

    description:
    Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
    All elements < k are moved to the left
    All elements >= k are moved to the right
    Return one partitioning index, i.e the first index i nums[i] >= k. If all elements in nums are smaller than k, then return nums.length. 
    
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        # this is a recursion question
        

        if len(nums) <= 0:
            return 0
        
        nums.sort()

        if k not in nums:
            if nums[-1] >= k:
                return 0
            return len(nums)
        
        for idx, each_num in enumerate(nums):
            if each_num >= k:
                return idx


