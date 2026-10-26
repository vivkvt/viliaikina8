n = int(input("n: "))
m = int(input('m: '))
a = [list(map(int, input().split())) for _ in range(n)]
b = []
for j in range(m):
    col_zeros = all(a[i][j] == 0 for i in range(n))
    b.append(col_zeros)
print(b)