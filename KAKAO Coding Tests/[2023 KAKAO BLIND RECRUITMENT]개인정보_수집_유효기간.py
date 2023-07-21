# 2023 KAKAO BLIND RECRUITMENT
# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def dateSplit(date):
    results = list(map(int, date.split('.')))
    return results[2] + results[1] * 28 + results[0] * 28 * 12

def solution(today, terms, privacies):
    tday = dateSplit(today)

    # New Dict to Store "a 12" to {'a': 12 * 28}
    termsDict = {a : int(b) * 28 for pair in terms for a,b in [pair.split()]}

    result = []
    for i in range(len(privacies)):
        day, code = privacies[i].split()
        day = dateSplit(day)
        if  day + termsDict[code] <= tday:
            result.append(i+1)
            
    return result

### Test Cases ###

terms = ['A 6', 'B 12', 'C 3']
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
today = "2022.05.19"
print(solution(today, terms, privacies))

terms1 = ["Z 3", "D 5"]
privacies1 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
today1 = "2020.01.01"
print(solution(today1, terms1, privacies1))


# Debugging
# tday = dateSplit(today)

# # New Dict to Store "a 12" to {'a': 12 * 28}
# termsDict = {a : int(b) * 28 for pair in terms for a,b in [pair.split()]}

# # New Dict to Store Privacy Dates and Terms
# # privDict = {a : b for pair in privacies for a,b in [pair.split()]}
# # privDict = {dateSplit(key): value for key, value in privDict.items()}

# # exp_days = []
# # for pk, pv in privDict.items():
# #     exp_days.append(pk + termsDict[pv])

# # result = []
# # for i in range(len(exp_days)):
# #     if exp_days[i] <= tday:
# #         result.append(i+1)


# -----------------------------------------------------------------------------------------
### Using datetime library


# import datetime
# from dateutil.relativedelta import relativedelta

# def solution(today, terms, privacies):
#     dt_today = datetime.datetime.strptime(today, "%Y.%m.%d")
    
#     # New Dict to Store "a 12" to {'a': 12}
#     termsDict = {a : int(b) for pair in terms for a,b in [pair.split()]}
    
#     # New Dict to Store Privacy Dates and Terms
#     privDict = {a : b for pair in privacies for a,b in [pair.split()]}
#     privDict = {datetime.datetime.strptime(key, "%Y.%m.%d"): value 
#                 for key, value in privDict.items()}

#     exp_date = []
#     for key, value in privDict.items():
#         for k, v in termsDict.items():
#             if k == value:
#                 exp_date.append(key + relativedelta(months = v))
#     print(exp_date)
#     result = []
#     for i in range(len(exp_date)):
#         if exp_date[i] <= dt_today:
#             result.append(i+1)
    
#     return result
