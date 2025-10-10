def solution(babbling):
    answer = 0
    
    for word in babbling:
        while True:
            if word[0:2] == "ye":
                word = word[2:len(word)]
            elif word[0:2] == "ma":
                word = word[2:len(word)]
            elif word[0:3] == "woo":
                word = word[3:len(word)]
            elif word[0:3] == "aya":
                word = word[3:len(word)]
            else:
                break
        if len(word) == 0:
            answer += 1

    return answer