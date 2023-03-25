def solution(N):
    ans = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        ans += N // coin
        N = N % coin
    return ans