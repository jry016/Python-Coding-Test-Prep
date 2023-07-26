# ----------------------------------------------------------------------------------
# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def brackets(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    
    if stack != []:
        return False
                
    return True

# Test Cases
print(brackets("()()"))
print(brackets("(())()"))
print(brackets(")()("))
print(brackets("(()("))

# Alternative Solution ----------------------------------------------------------
    # OPEN = '('
    # CLOSE = ')'
    # count = 0

    # for char in s:
    #     if char == OPEN:
    #         count += 1
    #     if char == CLOSE:
    #         count -= 1
    #     # count값이 0보다 작아졌다는 뜻은, 이미 짝이 맞지 않는다는 뜻이므로 early return
    #     # ex: '())', ')(' 이런 경우
    #     if count < 0:
    #         return False

