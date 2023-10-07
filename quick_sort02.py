from typing import List


class Solution:
    """
    
    @param numbers: unsorted integer array 

    @return: A new sorted integer array

    description: quick sort a list of integers


    """
    def quick_sort(self, nums: List[int]) -> int:
        # write your code herez
        print(nums)
        
        n = len(nums)

        if n <= 1:
            return nums
        pivot = nums[n-1] #pivot is always the last element
        left, right = 0, n-1
        while left < right:
            while nums[left] < pivot and left < right:
                left += 1
            
            while nums[right] >= pivot and left < right:
                right -= 1
            

            #if both conditions above do not meet, we swap
            nums[left], nums[right] = nums[right], nums[left] # note --> when right = left, here does nothing
            print("nums", nums)

        if left == right:  #when left == right, swap the left element with pivot
            nums[left], nums[n-1] = nums[n-1], nums[left]
            

        sorted_left = self.quick_sort(nums[:left])
        sorted_right = self.quick_sort(nums[right + 1:])
        return sorted_left + [pivot] + sorted_right # you need to return the sorted array here. 
    
    def sort_list(self, nums: List[int]) -> List[int]:
        
        return self.quick_sort(nums)
            
                

new_solution = Solution()
A = [1,2,3,4]
B = [2,4,5,6]
C = [5, 3, 1, 2, 4]
result = new_solution.quick_sort(C)
print("result", result)