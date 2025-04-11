import sys

input = sys.stdin.readline

N, state = map(int, input().split())
G_given_G, B_given_G, G_given_B, B_given_B = map(float, input().split())

# p(G_t|G_p) p(B_t|G_p) p(G_t|B_p) p(B_t|B_p)

if state == 0:
    p_cur_G, p_cur_B = 1, 0

else:
    p_cur_G, p_cur_B = 0, 1

date = 0
while date < N:
    p_next_G = p_cur_G * G_given_G + p_cur_B * G_given_B
    p_next_B = p_cur_G * B_given_G + p_cur_B * B_given_B
    date += 1

    p_cur_G, p_cur_B = p_next_G, p_next_B

print(round(p_cur_G * 1000))
print(round(p_cur_B * 1000))