n = int(input())
a, k = [[0 for j in range(n)] for i in range(n)], 1
q,w,e,r,c = 0,0,0,0,0
if n > 1:
    while k <= n**n and c <= n-1:
        q = k
        for i in range(n-2*c):
            a[c][i+c] = q
            q += 1
        w = q
        for j in range(n-1-2*c):
            a[j+1+c][n-1-c] = w
            w += 1
        e = w
        for i in range(n-1-2*c):
            a[n-1-c][n-2-i-c] = e
            e += 1
        r = e
        for j in range(n-2-2*c):
            a[n-2-j-c][c] = r
            r += 1
        k = r
        c += 1
    for i in range(n):
        print(*a[i])
else: print(1)
