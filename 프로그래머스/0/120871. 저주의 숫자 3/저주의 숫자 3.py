def solution(n):
    not3_list = []
    i = 1
    while len(not3_list) <= 100:
        if i % 3 != 0 and "3" not in str(i):
                not3_list.append(i)
        i += 1

    answer = not3_list[n - 1]
        
    return answer