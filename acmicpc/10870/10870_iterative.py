# iterative
def fibonacci(n):
    a = [0, 1, 1]
    if n < 3:
        ans = a[n]
    else:
        for i in range(n-2):
            a[0] = a[1]
            a[1] = a[2]
            a[2] = a[0]+a[1]
        ans = a[2]
    return ans

n = int(input())
print(fibonacci(n))