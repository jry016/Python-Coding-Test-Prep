# 2018 KAKAO BLIND RECRUITMENT
# [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def toBinaryStr(n, num):
    binary = str(bin(num)[2:]) # remove the prefix '0b' from the binary string.
    binary = binary.zfill(n)   # add leading zeros
    binStr = ""
    for character in binary:
        if(character == '0'):
            binStr += ' '
        else:
            binStr += '#'
    return binStr

def secretMap(n, arr1, arr2):
    map1 = []
    map2 = []
    for num1 in arr1:
        map1.append(toBinaryStr(n, num1))
    
    for num2 in arr2:
        map2.append(toBinaryStr(n, num2))
    
    final_map = []
    
    # zip map1 and 2 to iterate over corresponding elements simultaneously
    for strA, strB in zip(map1, map2):
        row = ""
        # zip strA and strB from map1 and 2 to be compared.
        for charA, charB in zip(strA, strB):
            if charA == '#' or charB == '#':
                row += '#'
            else:
                row += ' '
        final_map.append(row)
        
    return final_map

# Test Case
n1 = 5
a1 = [9, 20, 28, 18, 11]
a2 = [30, 1, 21, 17, 28]
print(secretMap(n1, a1, a2))

n2 = 6
b1 = [46, 33, 33 ,22, 31, 50]
b2 = [27 ,56, 19, 14, 14, 10]
print(secretMap(n2, b1, b2))