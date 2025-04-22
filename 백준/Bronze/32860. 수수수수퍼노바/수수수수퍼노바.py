# 26 진법
year, idx = map(int, input().split())

i = idx // 26
ii = idx % 26

if ii == 0:
    if i == 1:
        label = f"Z"
    else:
        label = f"{chr(i - 2 + 97)}z"
else:
    if i == 0:
        label = f"{chr(ii - 1 + 65)}"
    else:
        label = f"{chr(i - 1 + 97)}{chr(ii - 1 + 97)}"

print(f"SN {year}{label}")