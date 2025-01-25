def solution(n):
    n_count = len(bin(n)[2:].replace('0',''))
    
    while True:
        n += 1
        new_count = len(bin(n)[2:].replace('0',''))
        
        if n_count == new_count:
            return n
        
        