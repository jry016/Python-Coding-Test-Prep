# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 

def solution(lottos, win_nums):
    # List to Hold MAX and MIN Ranking of Lotto Result
    result = []
    
    # Ranking Key
    key = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }

    cnt = 0 # counter variable to track # of matching elements
    zcnt = 0 # counter variable to track # of zeros
    
    for i in range(len(lottos)):
        if(lottos[i] == 0): # zcnt = lottos.count(0)
            zcnt += 1
        for j in range(len(win_nums)):
            if(lottos[i] == win_nums[j]):
                cnt += 1
    
    # Future Reference
    # for x in win_nums:
    #     if x in lottos:
    #         cnt += 1
    
    max_rank = key[cnt + zcnt]
    min_rank = key[cnt]
    result.append(max_rank)
    result.append(min_rank)
   
    return result

# Test Case
l1 = [44, 1, 0, 0, 31, 25]
w1 = [31, 10, 45, 1, 6, 19]
print(solution(l1, w1))

l2 = [0, 0, 0, 0, 0, 0]
w2 = [38, 19, 20, 40, 15, 25]
print(solution(l2, w2))

l3 = [45, 4, 35, 20, 3, 9]
w3 = [20, 9, 3, 45, 4, 35]
print(solution(l3, w3))