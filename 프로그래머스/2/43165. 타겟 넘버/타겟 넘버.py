def solution(numbers, target):
    def calculate(prev, idx):
        if idx == len(numbers):
            return 1 if prev == target else 0
        
        return (calculate(prev + numbers[idx], idx + 1) +
                calculate(prev - numbers[idx], idx + 1))
    
    return calculate(0, 0)
