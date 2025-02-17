N = int(input())

candies = []
for _ in range(N):
    candy = int(input())
    candies.append(candy)

total_canides = sum(candies)//2

except_1 = 0
for i in range(1, N, 2):
    except_1 += candies[i]

each_candy = [total_canides - except_1]
for candy_sum in candies[:-1]:
    each_candy.append(candy_sum - each_candy[-1])

for c in each_candy:
    print(c)