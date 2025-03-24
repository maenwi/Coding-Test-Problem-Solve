inputs = []
max_length = -1
for _ in range(5):
    input_list = list(input())
    length = len(input_list)
    inputs.append({idx : v for idx, v in enumerate(input_list)})

    if max_length <= length:
        max_length = length

string = ""
for idx in range(max_length):
    for input_l in inputs:
        string = f"{string}{input_l.get(idx, "")}"

print(string)

