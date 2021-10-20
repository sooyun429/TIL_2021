# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, T):
    # write your code in Python 3.6

    typeCheck = ["P", "G", "M"]
    timeCheck = [0, 0, 0]

    for i in range(len(T)): # "PGP"
        for j in range(3): # 일치하는 typeCheck 인덱스 확인
            if typeCheck[j] in T[i]:
                distanceCheck = D[i]
                if i != 0:
                    for k in range(i-1, -1, -1):
                        if typeCheck[j] not in T[k]:
                            distanceCheck += D[k]
                        else:
                            break
                timeCheck[j] += (distanceCheck*2 + T[i].count(typeCheck[j]))
        
    return max(timeCheck)



# D = [2,5], T=["PGP", "M"]
# D = [3,2,4] T = ["MPM", "", "G"]
# D = [2,1,1,1,2] T = ["", "PP", "PP", "GM", ""]