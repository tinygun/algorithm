# recursive
def fibonacci(n):
    if n < 0:
        return
    elif n == 0: 
        return 0
    elif n <= 2:
        return 1
    
    answer = fibonacci(n-1)+fibonacci(n-2)
    return answer

n = int(input())
print(fibonacci(n))