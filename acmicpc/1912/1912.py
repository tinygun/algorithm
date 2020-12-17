total = int(input())
num_list = list(map(int, input().split()))
lst = [0 for a in range(total)]

for i in range(total):
    lst[i] = max(lst[i-1]+num_list[i], num_list[i])

print(max(lst))