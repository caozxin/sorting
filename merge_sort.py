from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Base case1: A list of size 1 or 0 is already sorted
    if n <= 1:
        return unsorted_list

    # Base case2: Split the list into left and right halves --> we need to always split into half first
    midpoint = n // 2
    left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    
    result_list = []
    left_pointer, right_pointer = 0, 0

    # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:  # If left list is empty, append element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:  # If right list is empty, append element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:  # Append smaller element from left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:  # Append smaller element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list

def merge_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list) 
    
    # split the list into two halfs until each unit is just only element
    if n > 1:
        #check if the number of the elements are odd or even
        if n % 2 == 0:
            half_max = int(n/2)
        else:
            half_max = int((n+1)/2)
        print('half_max', half_max)
        
        first_half, second_half = unsorted_list[: half_max], unsorted_list[half_max:]
        result_list = []
        print('first_half', first_half)
        print('second_half', second_half)
        merge_sort_list(first_half)
        merge_sort_list(second_half)
        pointer = half_max - 1

        print("pointer", pointer)
        # print('first_half[pointer]', first_half[pointer])
        # print('second_half[pointer]', second_half[pointer])
        print(" -------merging-----------")
        if first_half[pointer] > second_half[pointer]:
            result_list.append(second_half[pointer])
            result_list.append(first_half[pointer])
        else:
            result_list.append(first_half[pointer])
            result_list.append(second_half[pointer])

        print('result_list', result_list)
        pointer += 1

if __name__ == '__main__':
    example = [5, 3, 1, 2, 4]
    # print("input", example)
    sort_list = merge_sort_list
    result = sort_list(example)
    print("result", result)
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))

