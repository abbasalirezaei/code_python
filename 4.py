k = int(input())
n = 0
count = 0
while True:
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == k:
        print(n)
        break
    else:
        n += 1
        count = 0
