from typing import List

def swap(item1, position1, item2, position2):
    item1 = item2
    item2 = item1

def quick_sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list) 
    # print(unsorted_list)
    
    
    if n <= 1: #--> check if there is only one element
        return unsorted_list 
    pivot_pos = n-1
    pivot = unsorted_list[pivot_pos]
    start_pointer, end_pointer = 0, n-1
    print("beginning pivot, start_pointer, end_pointer: ")
    print(pivot, start_pointer, end_pointer)
    

    while start_pointer != end_pointer:
        print("pivot, start_pointer, end_pointer")
        print(pivot, start_pointer, end_pointer)

        
        if unsorted_list[start_pointer] >= pivot:
            end_pointer -= 1
            
        elif unsorted_list[start_pointer] < pivot:
            start_pointer += 1
        print("pivot, start_pointer, end_pointer")
        print(pivot, start_pointer, end_pointer)

        if unsorted_list[start_pointer] >= pivot and unsorted_list[end_pointer] < pivot:
            print("can swap:", unsorted_list[start_pointer], unsorted_list[end_pointer])
            unsorted_list[start_pointer], unsorted_list[end_pointer] = unsorted_list[end_pointer], unsorted_list[start_pointer]
        print("current list", unsorted_list)

    #swap the pivot with the one 1 step before it:
    unsorted_list[pivot_pos-1], unsorted_list[pivot_pos] = unsorted_list[pivot_pos], unsorted_list[pivot_pos-1]
    print("current list", unsorted_list)
    quick_sort_list(unsorted_list[:pivot_pos-1])

if __name__ == '__main__':
    unsorted_list = [5, 3, 1, 2, 4]
    # print("input", example)
    sort_list = quick_sort_list
    result = sort_list(unsorted_list)
    # print("result", result)
    # unsorted_list = [int(x) for x in input().split()]
    # res = sort_list(unsorted_list)
    # print(' '.join(map(str, res)))