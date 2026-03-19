import numpy as np


def check_simplex_code(m=3):
    n = 2 ** m - 1
    H_columns = []
    for i in range(1, 2 ** m):
        col = np.zeros(m, dtype=int)
        for j in range(m):
            col[j] = (i >> j) & 1
        H_columns.append(col)
    H = np.stack(H_columns, axis=1)

    print(f"Для m = {m}:")
    print("Размер матрицы H:", H.shape)

    codeword_weights = []
    for i in range(2 ** m):
        u = np.array([(i >> j) & 1 for j in range(m)], dtype=int)
        cw = np.dot(u, H) % 2
        weight = np.sum(cw)
        codeword_weights.append(int(weight))

    print("Веса всех кодовых слов дуального кода:", codeword_weights)
    nonzero_weights = [w for w in codeword_weights if w != 0]
    unique_nonzero = set(nonzero_weights)
    expected_weight = 2 ** (m - 1)
    is_simplex = len(unique_nonzero) == 1 and list(unique_nonzero)[0] == expected_weight

    print(f"Количество кодовых слов: {2 ** m}")
    print(f"Ожидаемый вес ненулевых слов: {expected_weight}")
    print(f"Фактические веса ненулевых слов: {unique_nonzero}")
    print(f"Это симплекс-код? {is_simplex}\n")
    return is_simplex


check_simplex_code(3)
check_simplex_code(4)
check_simplex_code(5)
check_simplex_code(9)