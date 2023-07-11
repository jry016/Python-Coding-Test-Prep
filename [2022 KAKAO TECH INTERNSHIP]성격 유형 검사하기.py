# 2022 KAKAO TECH INTERNSHIP
# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666


def personalityChecker(survey, choices):
    scoreKey = {
        "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0
    }
    scores = {
        1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3
    }
    
    i = 0
    for substr in survey: 
        if choices[i] in [1, 2, 3]:
            scoreKey[substr[0]] += scores[choices[i]]
        else:
            scoreKey[substr[1]] += scores[choices[i]]
        i += 1
          
    groups = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    personality = ""
    
    for group in groups:
        key1, key2 = group
        
        if scoreKey[key1] > scoreKey[key2]:
            personality += key1
            
        elif scoreKey[key1] < scoreKey[key2]:
            personality += key2
            
        elif scoreKey[key1] == scoreKey[key2]:
            if(scoreKey[key1] > scoreKey[key2]):
                personality += key2
            else:
                personality += key1
                
    return personality

# Test Cases
survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]    
print(personalityChecker(survey1, choices1)) # Expected Output: "TCMA"

survey2 = ["TR", "RT", "TR"]
choices2 = [7, 1, 3]
print(personalityChecker(survey2, choices2)) # Expected Output: "RCJA"

