# 2018 KAKAO BLIND RECRUITMENT
# [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def dartScoring(dartResult):
    temp = []
    current_score = ""
    
    for character in dartResult:
        if character.isdigit():
            current_score += character
            
        elif character == 'S':
            temp.append(int(current_score) ** 1)
            current_score = ""
        
        elif character == 'D':
            temp.append(int(current_score) ** 2)
            current_score = ""
        
        elif character == 'T':
            temp.append(int(current_score) ** 3)
            current_score = ""
        
        elif character == '*':
            if len(temp) >= 2:
                temp[-2] *= 2   # multiply 2 to the first value
            temp[-1] *= 2       # multiply 2 to the value before current
        
        elif character == '#':
            temp[-1] *= -1
    
    return sum(temp)

# Test Cases
print(dartScoring("1S2D*3T"))
print(dartScoring("1D2S#10S"))
print(dartScoring("1D2S0T"))
print(dartScoring("1S*2T*3S"))
print(dartScoring("1D#2S*3S"))
print(dartScoring("1T2D3D#"))
print(dartScoring("1D2S3T*"))