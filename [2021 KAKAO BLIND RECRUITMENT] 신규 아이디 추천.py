# 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천
# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
#

def CreateID(new_id):
    
    # Step 1 Lower-case
    new_id = new_id.lower()
    
    answer = ""
    
    # Step 2 Strip Non alphabet, number, -, _, . characters
    for s in new_id:
        if (s.isalpha() or s.isdigit() or s in ['.', '-', '_']):
            answer += s
    
    # Step 3 Convert multiple ... to .
    while ".." in answer:
        answer = answer.replace("..", '.')
    
    # Step 4 Strip . if at the front or end of the string
    if(answer[0] == '.'):
        if (len(answer) > 1):
            answer = answer[1:]
        else:
            answer = '.'
    if(answer[-1] == '.'): 
        answer = answer[:-1]
        
    # Step 5: If new_id = empty --> new_id = 'a'
    if(answer == ''):
        answer = 'a'
    
    # Step 6: If len(new_id) > 16 -- strip remaining
    if(len(answer) > 15):
        answer = answer[:15]
        if(answer[-1] == '.'):
            answer = answer[:-1]
    
    # Step 7: If len(new_id < 3) -- repeat the last character so that the id is at least len = 3
    while(len(answer) < 3):
        answer = answer + answer[-1]
        
    return answer

s1 = "...!@BaT#*..y.abcdefghijklm"
s2 = "z-+.^."
s3 = "=.="
s4 = "123_.def"
s5 = "abcdefghijklmn.p"

print(CreateID(s1))
print(CreateID(s2))
print(CreateID(s3))
print(CreateID(s4))
print(CreateID(s5))