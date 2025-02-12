from itertools import product

T = int(input())
Ns = []

for _ in range(T):
    Ns.append(int(input()))

for N in Ns:
    operations = list(product(["+", "-", " "], repeat = N - 1))
    answers = []

    for operation in operations:
        just_for_print = []
        expression = ""
        for i in range(N - 1):
            just_for_print.append(str(i + 1))
            just_for_print.append(operation[i])

            expression = f"{expression}{i + 1}{operation[i]}"

        just_for_print.append(str(N))
        expression = f"{expression}{N}"

        expression = expression.replace(" ","")
        
        answer = eval(expression)
        
        if answer == 0:
            answers.append("".join(just_for_print))
    
    answers.sort()
    for a in answers:
        print(a)
    
    if N != Ns[-1]:
        print()