def solution(brown, yellow):
    # yellow의 변의 길이 + 4 = brown 개수
    # yellow의 (세로 + 가로) * 2 = brown의 개수 - 4
    yellow_h = 1
    
    while True:
        yellow_r = yellow / yellow_h
        
        if brown - 4 == (yellow_h + yellow_r) * 2:
            break
        yellow_h += 1

        
    return [yellow_r + 2, yellow_h + 2]
        
        
    
        