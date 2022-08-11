d = int(input())

h = d // (360 // 12)
m = d % (360 // 12) * 60 // (360 // 12)

print('It is', h, 'hours', m, 'minutes.', sep=' ')
