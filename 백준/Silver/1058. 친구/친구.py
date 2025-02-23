# 2-친구
# 바로 내 친구거나,
# 한 다리 건너서 친구거나

N = int(input())
friends = []
for _ in range(N):
    relationship = list(input())
    relationship = [i for i, r in enumerate(relationship) if r == "Y"] # Y인 경우 친구로 추가
    friends.append(relationship)

super_inssa = -1
for person in range(N):
    two_friends_list = []
    for friend_1 in friends[person]:
        # 친구의 친구 검색
        if friend_1 not in two_friends_list:
            two_friends_list.append(friend_1)

        for friend_2 in friends[friend_1]:
            if friend_2 != person and friend_2 not in two_friends_list:
                two_friends_list.append(friend_2)
    
    # 반복문이 끝나면, 친구의 친구 search가 끝났다는 것.
    # 슈퍼인싸 갱신
    super_inssa = max(super_inssa, len(two_friends_list))

print(super_inssa)