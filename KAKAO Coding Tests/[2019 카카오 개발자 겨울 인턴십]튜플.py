# 2019 카카오 개발자 겨울 인턴십
# 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    
    substr = s.strip("{}").split("},{")
    input_tuple = [list(map(int, sub.split(","))) for sub in substr]
    sorted_tuple = input_tuple.sort(input_tuple, key = len)
    
    result = []
    for sublist in sorted_tuple:
        for i in sublist:
            if i not in result:
                result.append(i)
        
    return result

# Test Cases
s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"  # [2, 1, 3, 4]
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"  # [2, 1, 3, 4]
s3 = "{{20,111},{111}}"               # [111, 20]
s4 = "{{123}}"                        # [123]
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"  # [3, 2, 4, 1]

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))

 