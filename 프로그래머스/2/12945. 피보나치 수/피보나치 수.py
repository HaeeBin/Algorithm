def solution(n):
    F = []
    for i in range(n+1):
        if i <= 1:
            F.append(i)
        else:
            F.append(F[i-1]+F[i-2])
    return F[n] % 1234567