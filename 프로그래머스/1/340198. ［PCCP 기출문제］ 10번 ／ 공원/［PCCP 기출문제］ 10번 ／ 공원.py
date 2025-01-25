def can_sit(park, r, c):
    if park[r][c] == "-1":
        return True
    else:
        return False

def solution(mats, park):
    park_sit = [[0 for i in range(len(park[0]) + 1)] for j in range(len(park) + 1)]
    largest = 0
    
    for r in range(1, len(park_sit)):
        map_r = r - 1
        for c in range(1, len(park_sit[0])):
            map_c = c - 1

            if can_sit(park, map_r, map_c):
                park_sit[r][c] = min(park_sit[r - 1][c], park_sit[r - 1][c - 1], park_sit[r][c - 1]) + 1
                if park_sit[r][c] > largest and park_sit[r][c] in mats:
                    largest = park_sit[r][c]
            
            else:
                continue

    # for r in range(1, len(park_sit)):
    #     print(park_sit[r])
    if largest == 0:
        return -1
    return largest


