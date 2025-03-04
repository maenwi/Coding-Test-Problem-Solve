N = int(input())

numbers = input().split()

numbers.sort(key = lambda x: x * 10, reverse = True)

if numbers[0] == "0":
    print("0")
else:
    print("".join(numbers))