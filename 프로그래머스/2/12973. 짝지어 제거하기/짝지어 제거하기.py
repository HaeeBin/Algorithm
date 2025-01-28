def solution(s):
    result = []
    for i in s:
        if len(result) == 0:
            result.append(i)
        else:
            if result[-1] == i:
                result.pop()
            else:
                result.append(i)
    if len(result) == 0:
        return 1
    else:
        return 0
