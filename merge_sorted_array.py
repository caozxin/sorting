from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array

    description: Merge two given sorted ascending integer array A and B into a new sorted integer array.

    A = [1]
    B = [1]
    Output: [1,1]

    A = [1,2,3,4]
    B = [2,4,5,6]
    Output: [1,2,2,3,4,4,5,6]

    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        # we continue to check a and b until all numbers are checked
        n = len(a)
        m = len(b)

        new_array = [ float() ] * (n +m)
        print(new_array)
        result_list = []
        for i in range(n):
            new_list = []
            if len(result_list) <= 0:
                if a[i] <= b[i]:
                    new_list.append(a[i])
                    new_list.append(b[i])
                else:
                    new_list.append(b[i])
                    new_list.append(a[i])
            else:
                pivot = result_list[0][-1]

                if a[i] <= pivot and b[i] < pivot:
                    new_list.append(a[i])
                    new_list.append(pivot)
                    new_list.append(b[i])
                elif a[i] > pivot and b[i] <= pivot:
                    new_list.append(b[i])
                    new_list.append(pivot)
                    new_list.append(a[i])

            if len(result_list) <= 0:
                result_list.append(new_list)
            result_list[-1] = new_list
            print("new_list, result_list")
            print(new_list, result_list)

    def merge_sorted_array02(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        # we continue to check a and b until all numbers are checked
        """
        To merge two sorted lists:
        1) two pointers from the same direction and check if which one is the smaller one
        to add into the result_list.
        2) when it is added, the pointer will be +=1
        3) if one list is empty, we will append element from anoterh list
        4) loop ends when both lists' elemements are added in the result_list
        """
        n = len(a)
        m = len(b)

        result_list = []
        a_idx, b_idx = 0, 0
        while a_idx < n or b_idx < m:
            if a_idx == n:
                result_list.append(b[b_idx])
                b_idx += 1
            elif b_idx == m:
                result_list.append(a[a_idx])
                a_idx += 1
            elif a[a_idx] <= b[b_idx]:
                result_list.append(a[a_idx])
                a_idx += 1
            elif a[a_idx] > b[b_idx]:
                result_list.append(b[b_idx])
                b_idx += 1

                
        print("result_list", result_list)
        return result_list
    

new_solution = Solution()
A = [1,2,3,4]
B = [2,4,5,6]
result = new_solution.merge_sorted_array02(A,B)
print("result", result)