n, k = int(input()), int(input())
k_start = k

circle = [i for i in range(1, n + 1)]
print(circle)

while True:
    if len(circle) == k_start - 1:
        break
    elif k <= len(circle):
        circle.pop(k-1)
        print(circle)
        k += k_start
        # print(k)
    else:
        k = k_start

print(circle)
