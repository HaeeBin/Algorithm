def solution(A,B):
    A.sort()
    B.sort()
    sum = 0
    
    for i in B[::-1]:
        sum += A.pop(0) * i
    
    return sum