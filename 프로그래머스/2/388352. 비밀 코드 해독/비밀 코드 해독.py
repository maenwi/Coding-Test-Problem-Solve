# 최악의 경우 : 30C5 개의 조합을 확인해야함

from itertools import combinations

def solution(n, q, ans):
    m = len(q)
    
    answer = 0
    
    candidates = list(combinations(range(1,n+1), 5))
    
    for candidate in candidates:
        is_possible = False
        for i in range(m):
            # q[i]와 comb에 겹치는 숫자들의 개수가 ans[i]와 같다면?
            if len(set(q[i]) & set(candidate)) == ans[i]:
                is_possible = True
            else:
                # 같지 않다면 불가능한 후보 임으로 확인할 필요도 없음
                is_possible = False
                break
        
        if is_possible: # 가능한 후보를 찾았다면
            answer += 1
            
    return answer