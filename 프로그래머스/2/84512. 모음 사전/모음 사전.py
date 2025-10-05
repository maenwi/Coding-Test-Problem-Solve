from itertools import product

def solution(word):
    words = []
    for l in range(1, 6):
        words.extend(list(product("AEIOU", repeat = l)))
        
    words.sort()
        
    for i in range(len(words)):
        if word == "".join(words[i]):
            return i + 1
    