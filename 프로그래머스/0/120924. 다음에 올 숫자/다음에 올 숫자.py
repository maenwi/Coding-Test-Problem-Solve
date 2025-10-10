def solution(common):
    length = len(common)

    diff = set()
    ratio = set()
    for i in range(0, length - 1):
        diff.add(common[i + 1] - common[i])
        if common[i] == 0: # 등비수열이 될 수 없음
            continue
        else:
            ratio.add(int(common[i + 1]/common[i]))

    if len(diff) == 1: #등차수열
        d = diff.pop()
        answer = common[length - 1] + d
    else: #등비수열. 왜냐하면 주어진 수열은 등차 혹은 등비이기 때문
        r = ratio.pop()
        answer = common[length - 1] * r
    
    return answer