n, k = map(int, input().split())

ans = 0
while n >= k:
    if n % k == 0:
        n /= k
        ans += 1
    else:
        ans += (n % k)
        n -= (n % k)
ans += (n - 1)
print(int(ans))