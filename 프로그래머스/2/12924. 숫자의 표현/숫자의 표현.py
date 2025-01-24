def solution(n):
    answer = 1
    for i in range(1, n+1):
        sum_n = 0
        sum_list = []
        for j in range(i, n+1):
            if sum_n > n:
                break
            elif sum_n == n:
                answer += 1
                break
            else:
                sum_n += j
                sum_list.append(j)
                
    return answer
