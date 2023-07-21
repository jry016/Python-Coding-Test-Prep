# 코딩 기초 트레이닝

# 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862
import re
def solution1(myStr):
    answer = []
    splitwords = '[abc]'
    answer = re.split(splitwords, myStr)
    answer = list(filter(None, answer))
    
    if len(answer) == 0:
        return ['EMPTY']
    
    return answer

# Test Cases
print(solution1("baconlettucetomato"))
print(solution1("cabab"))
