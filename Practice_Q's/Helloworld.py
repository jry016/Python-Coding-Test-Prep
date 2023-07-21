import numpy as np

# def solution(arr, k):

#     flatten_arr = np.ravel(arr)
#     sorted_arr = sorted(flatten_arr)
#     answer = sorted_arr[k-1]
            
#     return answer

def solution(arr, k):
    flatten_arr = []
    for sublist in arr:
        if isinstance(sublist, list):
            for element in sublist:
                flatten_arr.append(element)
        else:
            flatten_arr.append(sublist)
    sorted_arr = sorted(flatten_arr)
    answer = sorted_arr[k-1]
    return answer

print(solution([[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]], 4))
