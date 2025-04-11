import sys

input = sys.stdin.readline

Gunnar = sum(map(int, input().split()))
Emma = sum(map(int, input().split()))

if Gunnar > Emma:
    print("Gunnar")
elif Gunnar < Emma:
    print("Emma")
else:
    print("Tie")