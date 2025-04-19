n = int(input())
k = int(input())

numbers = [input() for _ in range(n)]
combined_numbers = set()

def backtrack(numbers, k, used, path, combined_numbers):
    if len(path) == k:
        combined_numbers.add(int("".join(path)))
        return 
    
    for i in range(len(numbers)):
        if i in used:
            continue
        used.add(i)
        backtrack(numbers, k, used, path + [numbers[i]], combined_numbers)
        used.remove(i)

backtrack(numbers, k , set(), [], combined_numbers)

print(len(combined_numbers))