def make_identity(N):
    identity = [[0] * N for _ in range(N)]

    for idx in range(N):
        identity[idx][idx] = 1
    
    return identity

def inner_product(vector_1, vector_2):
    result = 0
    for a, b in zip(vector_1, vector_2):
        result += (a * b)
    
    return result

def matrix_multi(LEFT, RIGHT, mod):
    nrow = len(LEFT)
    ncol = len(RIGHT[0])
    result = [[0] * ncol for _ in range(nrow)]

    for LEFT_row_idx in range(nrow):
        for RIGHT_col_idx in range(ncol):
            LEFT_row = LEFT[LEFT_row_idx]
            RIGHT_col = [RIGHT[RIGHT_row_idx][RIGHT_col_idx] for RIGHT_row_idx in range(len(RIGHT))]
            result[LEFT_row_idx][RIGHT_col_idx] = (inner_product(LEFT_row, RIGHT_col) % mod)
    
    return result

def matrix_power(matrix, power):
    result = make_identity(len(matrix))

    while power:
        if power % 2 == 1:
            result = matrix_multi(result, matrix, 1000)
        matrix = matrix_multi(matrix, matrix, 1000)
        power //= 2

    return result

matrix = []
N, B = map(int, input().split())
for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = matrix_power(matrix, B)
for row in result:
    print(" ".join([str(n) for n in row]))