# n 과 m - 1
n, m = map(int, input().split()) # n은 숫자 갯수, m은 수열 길이
number = [a+1 for a in range(n)] # 사용할 숫자 리스트
memo = [0] * n # 숫자 사용 체크용 
array = []
cnt = 0

def nm1(x):
    global cnt
    cnt+=1
    if x == m:
        print(*array) # 출력
        return
    
    for i in range(n):
        print(cnt, '전:',memo, array, i+1)
        if memo[i] == 1:               # 사용한 경우 패스
            continue
        
        array.append(number[i])      # 수열 추가
        memo[i] = 1            # 사용한 수 체크
    
        print(cnt, '중:',memo, array, i+1)
        nm1(x + 1)                        # + 1번째 수열을 위해 재귀함수 호출

        print(cnt, '후:',memo, array, i+1)
        array.pop()                       # 수열 마지막 자리 삭제
        memo[i] = 0           # 사용한 수 초기화
        
nm1(0)    