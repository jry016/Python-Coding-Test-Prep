# 2021 카카오 채용연계형 인턴십
# 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    key = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9
    }
    for word in key:
        s = s.replace(word, str(key[word]))
        
    return int(s)

# Test Cases
print(solution("one4seveneight")) #	1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123
