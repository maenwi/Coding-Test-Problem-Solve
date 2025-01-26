def matching(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for u, b in zip(list(user_id), list(banned_id)):
        if u != b:
            if b != "*":
                return False
    return True


def solution(user_ids, banned_ids):
    candidates = [[] for _ in banned_ids]
    for i, banned_id in enumerate(banned_ids):
        for user_id in user_ids:
            if matching(user_id, banned_id):
                candidates[i].append(user_id)

    def backtrack(index, selected, result):
        # 모든 서브리스트에서 원소를 선택했으면 결과 저장
        if index == len(candidates):
            results.append(result[:])
            return
        
        # 현재 서브리스트에서 선택 가능한 원소 탐색
        for element in candidates[index]:
            if element not in selected:  # 그 원소가 아직 선택되지 않았다면
                selected.add(element)   # 선택한 원소를 기록
                result.append(element)  # 결과에 추가
                
                backtrack(index + 1, selected, result)  # 다음 서브리스트로 이동
                
                # 백트래킹
                selected.remove(element)
                result.pop()
        
    results = []
    backtrack(0, set(), [])

    results = list(set(frozenset(r) for r in results))
    
    return len(results)
