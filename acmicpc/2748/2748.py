n = int(input())
answer, stack = 0, 1
for i in range(n):
    answer, stack = stack, answer + stack

print(answer)