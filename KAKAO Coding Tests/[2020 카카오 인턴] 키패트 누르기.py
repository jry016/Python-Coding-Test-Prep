# 2020 카카오 인턴십
# [카카오 인턴] 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

# def distanceCalc(pos, num, hand):
#     if(hand == "right"):
#         Rdistance_record = {
#             2: {2: 0, 5: 1, 8: 2, 0: 3},
#             3: {2: 1, 5: 2, 8: 3, 0: 4},
#             5: {2: 1, 5: 0, 8: 1, 0: 2},
#             6: {2: 2, 5: 1, 8: 2, 0: 3},
#             8: {2: 2, 5: 1, 8: 0, 0: 1},
#             9: {2: 3, 5: 2, 8: 1, 0: 2},
#             0: {2: 3, 5: 2, 8: 1, 0: 0}
#         }
#         return Rdistance_record[pos][num]
    
#     elif(hand == "left"):
#         Ldistance_record = {
#             1: {2: 1, 5: 2, 8: 3, 0: 4},
#             2: {2: 0, 5: 1, 8: 2, 0: 3},
#             4: {2: 2, 5: 1, 8: 2, 0: 3},
#             5: {2: 1, 5: 0, 8: 1, 0: 2},
#             7: {2: 3, 5: 2, 8: 1, 0: 2},
#             8: {2: 2, 5: 1, 8: 0, 0: 1},
#             0: {2: 3, 5: 2, 8: 1, 0: 0}
#         }
#         return Ldistance_record[pos][num]

def distanceCalc(pos, num):
    distance_record = {
           0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2],  
           1: [4, 0, 1, 2, 1, 2, 3, 2, 3, 4],
           2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
           3: [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
           4: [3, 1, 2, 3, 0, 1, 2, 1, 2, 3],
           5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
           6: [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
           7: [2, 2, 3, 4, 1, 2, 3, 0, 1, 2],
           8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1], 
           9: [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
           '*': [1, 3, 4, 5, 2, 3, 4, 1, 2, 3],
           '#': [1, 5, 4, 3, 4, 3, 2, 3, 2, 1]
    }
    return distance_record[pos][num]

def keypad(numbers, hand):
    answer = ''
    Lcurrent_pos = '*'
    Rcurrent_pos = '#'
    
    for i in range(0, len(numbers)):
        if (numbers[i] in [1, 4, 7]):
            answer += 'L'
            Lcurrent_pos = numbers[i]
            
        elif (numbers[i] in [3, 6, 9]):
            answer += 'R'
            Rcurrent_pos = numbers[i]
            
        elif (numbers[i] in [2, 5, 8, 0]):
            if(hand == 'right'): 
                if(distanceCalc(Lcurrent_pos, numbers[i]) >= distanceCalc(Rcurrent_pos, numbers[i])):
                    answer += 'R'
                    Rcurrent_pos = numbers[i]
                else:
                    answer += 'L'
                    Lcurrent_pos = numbers[i]
            else:
                if(distanceCalc(Rcurrent_pos, numbers[i]) >= distanceCalc(Lcurrent_pos, numbers[i])):
                    answer += 'L'
                    Lcurrent_pos = numbers[i]
                else:
                    answer += 'R'
                    Rcurrent_pos = numbers[i]
                        
    return answer


# Test Cases
num1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] # R
num2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2] # L
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] # R

print(keypad(num1, 'right'))
print(keypad(num2, 'left'))
print(keypad(num3, 'right'))

