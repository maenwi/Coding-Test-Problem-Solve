ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
OPERATOR = "+-*/"

def basic_operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b

N = int(input())
operation = list(input())

values = {}
for i in range(N):
    values[ALPHABET[i]] = int(input())

stack = []
for o in operation:
    if o in ALPHABET:
        stack.append(values[o])
    elif o in OPERATOR:
        r = stack.pop()
        l = stack.pop()

        stack.append(basic_operation(l, r, o))

print(f"{stack.pop():.2f}")