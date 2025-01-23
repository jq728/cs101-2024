row_a, col_a = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(row_a)]

row_b, col_b = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(row_b)]

row_c, col_c = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(row_c)]

if col_a != row_b:
    print("Error!")
else:
    D = [[sum(A[i][k] * B[k][j] for k in range(col_a)) for j in range(col_b)] for i in range(row_a)]

    if row_a != row_c or col_b != col_c:
        print("Error!")
    else:
        result = [[D[i][j] + C[i][j] for j in range(col_b)] for i in range(row_a)]

        for row in result:
            print(" ".join(map(str, row)))