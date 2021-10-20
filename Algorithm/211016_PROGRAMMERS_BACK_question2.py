a = [3,2,1,3]

print(a.sort())
print(a)


import itertools

def solution(leave, day, holidays):
    answer = 0
        
    # 주말 dict
    weekend = {'MON': [6, 7, 13, 14, 20, 21, 27, 28],
               'TUE': [5, 6, 12, 13, 19, 20, 26, 27], 
               'WED': [4, 5, 11, 12, 18, 19, 25, 26], 
               'THU': [3, 4, 10, 11, 17, 18, 24, 25], 
               'FRI': [2, 3, 9, 10, 16, 17, 23, 24, 30], 
               'SAT': [1, 2, 8, 9, 15, 16, 22, 23, 29, 30], 
               'SUN': [1, 7, 8, 14, 15, 21, 22, 28, 29]}
    # 쉬는 날
    off_day = list(set(weekend[day] + holidays))
    
    # 쉬지 않는 날
    not_off_day = []
    for i in range(1, 31):
        if i not in off_day:
            not_off_day += [i]
    # print(off_day)
    # print(not_off_day)

    # 일하는 날보다 연차가 많은 경우 결과값은 무조건 30일
    if (30-len(off_day)) <= leave:
        answer = 30
    else: # 아닌 경우 경우의 수 따져보는 계산 필요
        leave_combinations = list(itertools.combinations(not_off_day, leave)) # 연차 사용하는 날_조합
        # print(leave_combinations)
        
        for leave_combination in leave_combinations:
            temp_cnt = 0
            for i in range(1, 31):
                if (i in off_day) or (i in leave_combination):
                    temp_cnt += 1
                else:
                    if temp_cnt > answer:
                        answer = temp_cnt
                    temp_cnt = 0
    
        # for leave_combination in leave_combinations:
        #     total_off_day = list(set(list(leave_combination) + off_day))
        #     total_off_day.sort()
        #     temp_cnt = 1
            
        #     for i in range(1, len(total_off_day)):
        #         if total_off_day[i-1]+1 == total_off_day[i]:
        #             temp_cnt += 1
        #         else:
        #             if temp_cnt > answer:
        #                 answer = temp_cnt
        #             temp_cnt = 1

    return answer