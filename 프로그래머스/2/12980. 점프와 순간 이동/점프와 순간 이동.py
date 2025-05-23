def solution(n):
    result = 0
    
    while n > 2:
    
        if n % 2 != 0:
            n -= 1
            result += 1
        else:
            n /= 2
    
    return result + 1
        