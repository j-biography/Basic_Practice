
# 버블 정렬 구현

arr = [4,9,2,0,3,10,8,1]

def bubble(arr):
    n = len(arr)
    
    for i in range(n): # 배열의 요소 개수만큼 반복 N^2
        
        for j in range(n-i-1): # 배열 한바퀴
            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
bubble(arr)


# 23968

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
result = -1

for i in range(N):
    
    for j in range(N-i-1):
    
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1
            
            if count == K:
                result = f'{arr[j]} {arr[j+1]}'
                
print(result)
              
              
            
    
            


