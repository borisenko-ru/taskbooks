k = int(input())

h = k // 3600
m = k % 3600 // 60

print('It is {} hours {} minutes.'.format(h, m))
