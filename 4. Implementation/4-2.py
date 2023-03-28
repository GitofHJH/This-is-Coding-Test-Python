# n = int(input())

# count = 0
# for h in range(n+1):
#     for m in range(60):
#         for s in range(60):
#             if '3' in str(h) + str(m) + str(s):
#                 count += 1
#                 time = ''

# print(count)

N = int(input())

# 전체의 경우의 수
tmp1 = (N + 1) * 60 * 60
# 3이 하나도 포함되지 않는 경우
if N < 3:
    tmp2 = (N + 1) * 45 * 45
# 3이 1개 : 3
elif N < 13:
    tmp2 = N * 45 * 45
# 3이 2개 : 3 13
elif N < 23:
    tmp2 = (N - 1) * 45 * 45
# 3이 3개 : 3 13 23
else:
    tmp2 = (N - 2) * 45 * 45

print(tmp1 - tmp2)