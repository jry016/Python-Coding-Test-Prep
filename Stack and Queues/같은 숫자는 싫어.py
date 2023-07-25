# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def uniqueArr(arr):
    unique_elements = []
    
    for i in range(len(arr)):
        if i == (len(arr)-1) or arr[i] != arr[i+1]:
            unique_elements.append(arr[i])
    return unique_elements
 
# Test Cases
print(uniqueArr([1,1,3,3,0,1,1]))    
print(uniqueArr([4,4,4,3,3]))    

        

