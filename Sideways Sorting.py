# KATTIS CODING TEST PROBLEMS
# MIA
# https://nus.kattis.com/courses/CS2040/CS2040_S4_AY1718/assignments/f3bh9x/problems/mia

# boolean continueLoop = true;
#         while (continueLoop) {
#             String[] inputs = br.readLine().split(" ");
#             int row = Integer.parseInt(inputs[0]);
#             int col = Integer.parseInt(inputs[1]);
#             if (row == 0 && col == 0) {
#                 continueLoop = false;
#             } else {
#                 char[][] inputStrings = new char[col][row];

#                 for (int i = 0; i < row; i++) {
#                     String str = br.readLine();
#                     for (int j = 0; j < col; j++) {
#                         inputStrings[j][i] = str.charAt(j);
#                     }
#                 }


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
        return int(sorted(input, reverse = True))

s0, s1, r0, r1 = input().split()
while(True):
    #s0, s1, r0, r1 = input().split() # string
                                     # map(int, input().split())
    if(s0 == '0'):
        break
    
    p1_score = Mia(s0 + s1)
    p2_score = Mia(r0 + r1)
    
    if(p1_score > p2_score):
        print("Player 1 wins.")
    elif(p1_score < p2_score):
        print("Player 2 wins.")
    else:
        print("Tie.")
        
