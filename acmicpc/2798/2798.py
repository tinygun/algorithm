card_num, number = map(int, input().split())
card_list = sorted(list(map(int, input().split())), reverse=True)
answer = set()
for a in range(card_num):
    for b in range(a+1, card_num):
        for c in range(b+1, card_num):
            value = card_list[a]+card_list[b]+card_list[c]
            if value <= number:
                answer.add(value)
                break
                
print(max(answer))