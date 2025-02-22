s1 = input()
s2 = input()

def make_alphabet_num(s1) -> set:

    return_str1 = []
    d1 = {}
    for s in [s for s in s1]:
        if s not in d1.keys():
            d1[s] = 1
        else:
            d1[s] += 1
        return_str1.append(f"{s}{d1[s]}")

    return set(return_str1)

s1 = make_alphabet_num(s1)
s2 = make_alphabet_num(s2)

anagram_letters = len(s1.intersection(s2))

print(f"{len(s1) + len(s2) - 2*anagram_letters}")
