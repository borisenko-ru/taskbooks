k, n = map(int, input().split()) # 1<=k<=200 1<=n<=20000

p = n // k + 1 - n // k * k // n
s = n - (p - 1) * k

print(p, s)
