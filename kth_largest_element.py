from typing import (
    List,
)

class Solution:
    """
    Kth Largest Element

    @param k: An integer
    @param nums: An array
    @return: the Kth largest element

    description: Find the K-th largest element in an array. You can swap elements in the array. 1<= k <= 10^5

    k = 1
    nums = [1,3,4,2]
    output = 4

    k = 3
    nums = [9,3,2,4,8]
    output = 4

    """
    # def kth_largest_element(self, k: int, nums: List[int]) -> int:
    #     # write your code herez
    #     print(nums)
        
    #     n = len(nums)

    #     if n <= 1:
    #         return nums[0] if n == 1 else None # updated the base case to return None when there are no elements in the list 
        
    #     pivot = nums[n-1] #pivot is always the last element
    #     left, right = 0, n-1
    #     while left < right:
    #         while nums[left] < pivot and left < right:
    #             left += 1
            
    #         while nums[right] >= pivot and left < right:
    #             right -= 1
            

    #         #if both conditions above do not meet, we swap
    #         nums[left], nums[right] = nums[right], nums[left] # note --> when right = left, here does nothing
    #         print("nums", nums)

    #     if left == right:  #when left == right, swap the left element with pivot
    #         nums[left], nums[n-1] = nums[n-1], nums[left]
            
    #     # print("final nums", nums)
    #     # print(nums[:left], nums[right:])
    #     # print(nums[0:left], nums[left + 1 :])
    #     self.kth_largest_element(k, nums[:left])
    #     # self.kth_largest_element(k, nums[right + 1 :])

    #     # print("result nums", nums)
        
    #     sorted_left = self.kth_largest_element(k, nums[:left])
    #     sorted_right = self.kth_largest_element(k, nums[right + 1:])

    #     # return sorted_left + [pivot] + sorted_right # you need to return the sorted array here. 
    #     print(sorted_left, type(sorted_left))

        
    #     # if k == n - left:
    #     #     result = pivot
        
    #     # elif k < n - left:
    #     #     result = self.kth_largest_element(k, nums[left + 1:])
    #     # else:
    #     #     result =  self.kth_largest_element(k - (n - left), nums[:left])

    #     # return result
    
    # # def sort_list(self, k: int, nums: List[int]) -> int:
        
    # #     result = self.kth_largest_element(k, nums)
    # #     n = len(nums)
    # #     return result[n - k]

    def kth_largest_element02(self, k: int, nums: List[int]) -> int:
        # print(nums)
        
        n = len(nums)

        if n <= 1:
            return nums[0] if n ==  1 else None
        pivot = nums[n-1] #pivot is always the last element
        left, right = 0, n-1
        while left < right:
            while nums[left] < pivot and left < right: # compared with other two pointers, here should only be < 
                left += 1
            
            while nums[right] >= pivot and left < right:
                right -= 1
            

            #if both conditions above do not meet, we swap
            nums[left], nums[right] = nums[right], nums[left] # note --> when right = left, here does nothing
            # print("nums", nums)

        if left == right:  #when left == right, swap the left element with pivot
            nums[left], nums[n-1] = nums[n-1], nums[left]
            

        # sorted_left = self.kth_largest_element02(k, nums[:left])
        # sorted_right = self.kth_largest_element02(k, nums[right + 1:])
        # print(type(sorted_left), type(pivot))
        if k == n - left:
            return pivot
        elif k < n - left:
            return self.kth_largest_element02(k, nums[left + 1:])
        else:
            return self.kth_largest_element02(k - (n - left), nums[:left])

        print(result, type(result))
        # return sorted_left + [pivot] + sorted_right

new_solution = Solution()
k = 1
nums = [1,3,4,2]
nums02 = [5, 3, 1, 2, 4]
result = new_solution.kth_largest_element02(k, nums)
print("result", result)