n = int(input("Введите N: "))
m = int(input("Введите m: "))

if m > n:
    print("Ошибка: m должно быть не больше N")
    exit()
lst = list(map(float, input("Введите числа:").split()))
cur_sum = sum(lst[:m])
max_sum = cur_sum
for i in range(n-m):
    cur_sum = cur_sum - lst[i] + lst[i + m]
    max_sum = max(max_sum, cur_sum)
print(f"Максимальная сумма: {max_sum}")