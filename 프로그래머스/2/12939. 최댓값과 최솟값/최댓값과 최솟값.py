def solution(s):
    num_list = list(map(int,s.split()))
    
    max_num = max(num_list)
    min_num = min(num_list)
    
    return str(min_num) + ' ' + str(max_num)
    