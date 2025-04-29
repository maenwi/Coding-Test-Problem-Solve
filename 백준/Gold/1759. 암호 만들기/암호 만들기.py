from itertools import combinations

L, C = map(int, input().split())
alphabets = list(input().split())

mos = []
jas = []

while alphabets:
    alphabet = alphabets.pop()

    if alphabet in "aeiou":
        mos.append(alphabet)
    else:
        jas.append(alphabet)

passwords = []

for number_of_mo in range(1, L - 1):
    number_of_ja = L - number_of_mo

    possible_mos = list(combinations(mos, number_of_mo))
    possible_jas = list(combinations(jas, number_of_ja))
    
    for possible_mo in possible_mos:
        for possible_ja in possible_jas:
            password = list(possible_ja) + list(possible_mo)

            password.sort()

            passwords.append(password)

passwords.sort()

for password in passwords:
    print("".join(password))