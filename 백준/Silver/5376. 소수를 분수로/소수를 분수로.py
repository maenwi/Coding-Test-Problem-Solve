import sys
import re

input = sys.stdin.readline

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

N = int(input())
numbers = [input().strip().split(".")[1] for _ in range(N)]

for number in numbers:
    if "(" in number:
        repeat_and_nonrepeat = re.search(r'(\d*)\((\d+)\)', number)
        
        nonrepeat = repeat_and_nonrepeat.group(1)
        repeat = repeat_and_nonrepeat.group(2)

        denominator = int('9' * len(repeat) + '0' * len(nonrepeat))
        numerator = int(nonrepeat + repeat)
        if nonrepeat != "":
            numerator -= int(nonrepeat)
        
    else:
        denominator = int('1' + '0' * len(number))
        numerator = int(number)

    gcd = find_gcd(numerator, denominator)

    print(f"{numerator // gcd}/{denominator // gcd}")