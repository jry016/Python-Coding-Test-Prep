# 2022 KAKAO BLIND RECRUITMENT
# 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def fee_calc(fees, duration):
    if duration >= fees[0]:
        total_fee = fees[1] + math.ceil((duration - fees[0])/fees[2]) * fees[3]
    else: 
        total_fee = fees[1]
    return total_fee

def transform(records):
    records = [info.split() for info in records]
    records = [[sum(int(num) * 60**i for i, num in enumerate(reversed(part.split(':'))))] 
               + rest for part, *rest in records]
    return records

def solution(fees, records):
 
    # Transform Input as [[Minutes as of 00:00, License, Status], [Minutes as of 00:00, License, Status] ... ]
    records = transform(records)
    
    car_times = {}
    total_duration = {}
    
    for record in records:
        if record[1] not in car_times:
            # save license plate and duration to car_times dic
            car_times[record[1]] = record[0]
        
        else:
            if record[2] == 'OUT':
                if record[1] in total_duration:
                    total_duration[record[1]] += record[0] - car_times[record[1]]
                else:
                    total_duration[record[1]] = record[0] - car_times[record[1]]
                del car_times[record[1]]
                                
            elif record[2] == 'IN':
                car_times[record[1]] = record[0]
                
    for license in car_times:
        if license in total_duration:
            total_duration[license] += 1439 - car_times[license]
        else:
            total_duration[license] = 1439 - car_times[license]
    
    result = []
    # Calculate Fee
    for car in sorted(total_duration.keys()):
        result.append(fee_calc(fees, total_duration[car]))
    
    return result

# Test Cases:
f1 = [180, 5000, 10, 600]
r1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", 
      "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

f2 = [120, 0, 60, 591]
r2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

f3 = [1, 461, 1, 10]
r3 = ["00:00 1234 IN"]

print(solution(f1, r1))
print(solution(f2, r2))
print(solution(f3, r3))


# --- Trans function explanation ---
# 1.
# part, *rest in records: This uses extended unpacking to extract the first element of each sublist in the records list as part, and the rest of the elements (if any) as rest.
# 2.
# part.split(':'): This splits the part string (e.g., '05:34') into two substrings at the colon, resulting in a list like ['05', '34'].
# 3.
# reversed(part.split(':')): This reverses the order of the elements in the list obtained from the previous step, 
# resulting in an iterator that yields the elements in reversed order (e.g., ['34', '05']).
# 4. 
# enumerate(reversed(part.split(':'))): This function is used to iterate over the reversed list and returns a tuple of index and value. 
# For example, enumerate(['34', '05']) will yield (0, '34') and (1, '05'). The index and value are assigned to i and num, respectively, in the loop.
# 5.
# int(num) * 60**i: This multiplies the integer representation of the num (e.g., '34' -> 34) by 60 raised to the power of the index i. 
# For the example enumerate step above, it will calculate 34 * 60^0 = 34 and 5 * 60^1 = 300.
# 6.
# sum(...): This function sums up all the results obtained from the previous step. For the example enumerate step, it will calculate 34 + 300 = 334.
# 7. 
# [[sum(...)] + rest for ...]: This construct creates a new list that contains the calculated total time (in minutes) as the first element, followed by the rest of the elements 
# (i.e., the '5961' and 'IN' values) from the original sublist. For example, [[334, '5961', 'IN']].

def duration_calc(records, target):
    entry, exit, duration = None, None, None
    for record in records: 
        if record[1] == target:
            if record[2] == 'IN':
                entry = record[0]
            elif record[2] == 'OUT':
                exit = record[1]

        if entry is not None:
            duration = exit - entry
            break
        
    if exit is None and entry is not None:
        duration = 1439 - entry
        
    return duration














