# 2021 KAKAO BLIND RECRUITMENT
# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    menu_comb = {}
    
    for order in orders:
        for comb_length in course:
            # Get all combinations of the specified length for the current order
            combs = combinations(order, comb_length)
            
            for comb in combs:
                key = ''.join(sorted(comb))  # Sort the combination to ensure unique keys
                menu_comb[key] = menu_comb.get(key, 0) + 1
                
    filtered_comb = {key: value for key, value in menu_comb.items() if value > 1}
    
    # Find most chosen combination
    most_chosen = {}
    for comb_length in course:
        # Check if there are any unmatching results
        if not any(len(key)== comb_length for key in filtered_comb):
            continue  
        # Save the highest frequency key - value pair to most chosen
        most_chosen[comb_length] = max(value for key, value in filtered_comb.items()
                                       if len(key) == comb_length)
    
    menus = [key for key, value in filtered_comb.items()
             if value == most_chosen[len(key)]]
    menus.sort()
    return menus

# Test Cases
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))

orders1 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course1 = [2, 3, 5]
print(solution(orders1, course1))

orders2 = ["XYZ", "XWY", "WXA"]
course2 = [2,3,4]
print(solution(orders2, course2))

# Notes --------------------------------------------------------------------------------------------
# key = ''.join(sorted(comb)) ensures that the keys in the menu_comb dictionary are unique 
# because it sorts the elements in the current combination comb and then joins them together 
# as a single string.

# menu_comb.get(key, 0): This method retrieves the value associated with the key in the menu_comb dictionary. 
# If key is found in the dictionary, it returns the corresponding value. 
# If key is not found, it returns the default value, which is set to 0. 
# If key is present in the dictionary, it will get the current count of occurrences of that menu combination; 
# if key is not in the dictionary, it will get 0 as the default count.

# menu_comb[key] = menu_comb.get(key, 0) + 1: This line updates the count of occurrences for the specific menu combination. 
# It increments the count by 1 if the combination is already present in the dictionary (retrieved using .get()), 
# or it initializes the count to 1 if the combination is encountered for the first time (defaulting to 0 using .get()).



