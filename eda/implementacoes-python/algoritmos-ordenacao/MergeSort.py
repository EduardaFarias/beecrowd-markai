import time

def merge_Sort(array):
    start = time.time()
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        # Recursion
        merge_Sort(left_array)
        merge_Sort(right_array)

        # Merge
        left_index = 0 # Left array index
        right_index = 0 # Right array index
        merge_index = 0 # Merge array index

        while left_index < len(left_array) and right_index < len(right_array):

            if left_array[left_index] < right_array[right_index]:
                array[merge_index] = left_array[left_index]
                left_index += 1
            
            else:
                array[merge_index] = right_array[right_index]
                right_index += 1

            merge_index += 1

        while left_index < len(left_array):
            array[merge_index] = left_array[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right_array):
            array[merge_index] = right_array[right_index]
            right_index += 1
            merge_index += 1
    end =  time.time()

    return f'Run Time: {end - start:.10f} segs'


arr = [1, 6, 4, 8, 6, 55, 20, 1203, 44, 32, 78, 2, 0.8, 8, 6, 55, 20, 1203, 44, 32, 6, 4, 8, 6, 55]
print(merge_Sort(arr))

print(arr)