import re

inputs = []
while True:
    try:
        line = input().strip()
        if not line:
            break  # 빈 줄이면 종료
        inputs.append(line)
        
    except EOFError:
        break  # 입력 끝나면 종료 (예: Ctrl+D 또는 EOF 신호)

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

for number in inputs:
    j, s = number.split(".")

    if "(" in s:
        repeat_and_nonrepeat = re.search(r'(\d*)\((\d+)\)', s)
        
        nonrepeat = repeat_and_nonrepeat.group(1)
        repeat = repeat_and_nonrepeat.group(2)

        denominator = int('9' * len(repeat) + '0' * len(nonrepeat))
        numerator = int(nonrepeat + repeat)
        if nonrepeat != "":
            numerator -= int(nonrepeat)
        
    else:
        denominator = int('1' + '0' * len(s))
        numerator = int(s)

    if j != 0:
        numerator += int(j) * denominator

    gcd = find_gcd(numerator, denominator)

    print(f"{number} = {numerator // gcd} / {denominator // gcd}")