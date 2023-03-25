n, m, k = map(int, input().split())
data = list(map(int, input().split()))

max_1 = max(data)
data.remove(max_1)
max_2 = max(data)

bundle = max_1 * k + max_2
print(bundle * (m // (k + 1)) + max_1 * (m % (k + 1)))