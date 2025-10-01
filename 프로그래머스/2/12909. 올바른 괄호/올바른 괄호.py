def solution(s):
    number_of_open_parenthesis = 0
    for parenthesis in s:
        if parenthesis == ")":
            if number_of_open_parenthesis == 0:
                return False
            number_of_open_parenthesis -= 1
        else:
            number_of_open_parenthesis += 1
    
    if number_of_open_parenthesis == 0:
        return True
    else:
        return False