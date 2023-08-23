# LeetCode
# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75


from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        
        for i in asteroids:
            if not stack or i > 0:  # Always push positive asteroids to the stack
                                    # Only push negative asteroids when stack is empty
                stack.append(i)
            else:
                # Continuous simulation of collisions in the stack
                # Only Pop if: Stack is not empty and top asteroid is moving right(+) and has lower magnitude than current asteroid
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(i):
                    stack.pop()
                    
                # 2 Scenarios:
                # The top asteroid on the stack is moving left.
                # The stack is empty because the current asteroid exploded all right-moving asteroids.
                if not stack or stack[-1] < 0:  
                    stack.append(i)
                    
                elif stack[-1] == -i:  # Asteroids with same magnitude collide, continue without appending
                    stack.pop()         
                
        return list(stack)

# Test Cases
sol = Solution()
asteroids = [5,10,-5]
print(sol.asteroidCollision(asteroids)) # [5, 10]

asteroids = [8,-8]
print(sol.asteroidCollision(asteroids)) # []

asteroids = [10,2,-5]
print(sol.asteroidCollision(asteroids)) # [10]

# from typing import List
# from collections import deque

# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = deque()
#         stack.append(asteroids[0])
#         asteroids = asteroids[1:]
        
#         for i in asteroids:
#             if i > 0 and stack[-1] > 0:
#                 stack.append(i)
#             elif i < 0 and stack[-1] < 0:
#                 stack.append(i)
#             elif i > 0 and stack[-1] < 0:
#                 if abs(i) > abs(stack[-1]):
#                     stack.pop()
#                     stack.append(i)
#                 elif abs(i) == abs(stack[-1]):
#                     stack.pop()
#             elif i < 0 and stack[-1] > 0:
#                 if abs(i) > abs(stack[-1]):
#                     stack.pop()
#                     stack.append(i)
#                 elif abs(i) == abs(stack[-1]):
#                     stack.pop()
                
#         return list(stack)