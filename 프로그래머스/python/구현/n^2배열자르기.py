# 수식 생각해내는거 어렵..
def solution(n, left, right):
    answer = []
    
    
    for i in range(left, right+1):
        a = max(i//n, i%n) + 1
        answer.append(a)
 

    return answer    
    
