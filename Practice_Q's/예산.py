# Summer/Winter Coding(~2018)

# 예산 소팅 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/12982


# def solution2(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

def solution2(d, budget):
    answer = 0
    sorted_d = sorted(d)

    for i in sorted_d:
        budget = budget - i
        if budget < 0:
            break
        answer += 1
    return answer

print(solution2([1, 3, 2, 5, 4], 9))
print(solution2([2, 2, 3, 3], 10))