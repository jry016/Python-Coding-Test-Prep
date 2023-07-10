# KATTIS CODING TEST PROBLEMS
# MIA
# https://nus.kattis.com/courses/CS2040/CS2040_S4_AY1718/assignments/f3bh9x/problems/mia

def Mia(input):
    double_score = {
        "66" : 72, 
        "55" : 71, 
        "44" : 70, 
        "33" : 69, 
        "22" : 68, 
        "11" : 67
    }
    
    if (input in ["12", "21"]):
        return 73

    elif (input in double_score):
        return double_score[input]

    else:
        return int("".join(sorted(input, reverse = True)))

inputs = []

while True:
    line = input()
    
    # Terminating Condition
    if(line  == '0 0 0 0'):
        break
    
    inputs.append(line)
        
    for line in inputs:
        s0, s1, r0, r1 = line.split()
        p1_score = Mia(s0 + s1)
        p2_score = Mia(r0 + r1)
        
    if(p1_score > p2_score):
        print("Player 1 wins.")
    elif(p1_score < p2_score):
        print("Player 2 wins.")
    else:
        print("Tie.")
        

