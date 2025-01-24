def solution(s):
    
    remove_zero = 0
    count_change = 0
    
    while s != '1':
        count_change += 1
        
        num_1 = s.replace('0', '')
        remove_zero += len(s) - len(num_1)
        
        s = bin(len(num_1))[2:]
    
    return [count_change, remove_zero]