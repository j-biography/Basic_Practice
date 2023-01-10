# ACM Craft
# 위상정렬, '순서'를 찾아내는 알고리즘

'''

T = int(input())
XY_list = []

for test_n in range(T):
    
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    
    for rule_n in range(K):
        
        XY = list(map(int, input().split()))
        XY_list.append(XY)
       
        
    W = int(input())

    if XY_list[K][1] == W:
        print(XY_list[K])
        


print(D[W-1]) 
    
    
# print(XY[2])
# D[n-1]
    
'''  
  
###########################################
  
'''

T = 총 테스트 케이스 개수 (첫째 줄)

N / K = 총 건물의 개수 / 건설순서 규칙 개수(둘째 줄)

D = 각 건물의 건설에 걸리는 시간

X, Y = 건설 순서(X 건설 후에 Y 건설이 가능하다는 뜻)

W = 승리를 위해 건설해야 할 건물 번호

'''


T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    
    Rule = []
    Time = 0

    
    for j in range(K): 
        X,Y = map(int, input().split())
        Rule.append([X,Y])

    W = int(input())
    Count = W
    
    #####  데이터를 입력 받는 것은 여기까지  #####
    
    Time += D[W]
    while Count > 1:
        if Count == Rule[j][1]:
            Time += D[Rule[j][0]]
            Count -= (Count - Rule[j][0])
    
    
    
    
    # while Count <= W:
    #     if Rule[Count][0] == 1:
    #         Time += D[Count]
    
    
    # Count += Rule[선택한 줄][1]
    # >> 다시 Count += Rule
    # Count == Rule[0][Y] 
    
    # while Count < W:
        
    #     Time += D[Count] # 1번 건물부터 건설 소요 시간을 더함
    #     Count += 1

print(Time)