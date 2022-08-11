k = int(input())

k1 = k // 1000
k2 = k // 100 % 10
k3 = k // 10 % 10
k4 = k % 10

l = (k1 - k4) * 2 + (k2 - k3) * 3 + 1

print(l)
