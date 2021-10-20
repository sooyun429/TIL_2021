word = 'cow5'
print(word[:4])


def solution(registered_list, new_id):
    answer = ''
    while new_id in registered_list:
        for i in range(len(new_id)): # S와 N 분리작업
            if new_id[i] in '0123456789':
                S = new_id[:i]
                if i != len(new_id):
                    N = str(int(new_id[i:])+1)
                else: # new_id에 숫자가 없는 경우
                    N = '1'
                new_id = S + N
                break
        else: # new_id에 숫자가 없는 경우
            new_id += '1'
            
    answer = new_id
                
    return answer


def solution(registered_list, new_id):
    answer = ''
    while new_id in registered_list:
        for i in range(len(new_id)): # S와 N 분리작업
            if new_id[i] in '0123456789': # new_id에 숫자가 있는 경우
                S = new_id[:i]
                # if i != len(new_id):
                N = str(int(new_id[i:])+1)
                # else: # new_id에 숫자가 없는 경우
                #     N = '1'
                new_id = S + N
                break
        else: # new_id에 숫자가 없는 경우
            new_id += '1'
            
    answer = new_id
                
    return answer





def solution(registered_list, new_id):
    answer = ''
    
    for i in range(len(new_id)): # S와 N 분리작업
        if new_id[i] in '0123456789': # new_id에 숫자가 있는 경우
            S = new_id[:i]
            break
    else:
        S = new_id
        
    min_registered_list = []
    for registered_id in registered_list:
        if S in registered_id:
            min_registered_list += [registered_id]
    min_registered_list.sort()

    
    while new_id in min_registered_list:
        for i in range(len(new_id)): # S와 N 분리작업
            if new_id[i] in '0123456789': # new_id에 숫자가 있는 경우
                S = new_id[:i]
                N = str(int(new_id[i:])+1)
                new_id = S + N
                break
        else: # new_id에 숫자가 없는 경우
            new_id += '1'
            
    answer = new_id
                
    return answer



def solution(registered_list, new_id):
    answer = ''
    
    for i in range(len(new_id)): # S와 N 분리작업
        if new_id[i] in '0123456789': # new_id에 숫자가 있는 경우
            S = new_id[:i]
            N = new_id[i:]
            break
    else:
        S = new_id
        N = '0'
        
    min_registered_list = []
    for registered_id in registered_list:
        if S in registered_id:
            min_registered_list += [registered_id]
    min_registered_list.sort()

    
    while new_id in min_registered_list:
        new_id = S + str(int(N)+1)
            
    answer = new_id
                
    return answer



def solution(registered_list, new_id):
    
    for i in range(len(new_id)): # S와 N 분리작업
        if new_id[i] in '0123456789': # new_id에 숫자가 있는 경우
            S = new_id[:i]
            N = new_id[i:]
            break
    else:
        S = new_id
        N = '0'
        
    while new_id in registered_list:
        N = str(int(N)+1)
        new_id = S + N
                
    return new_id