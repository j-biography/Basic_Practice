# 백준 어린왕자
# 기하, 피타고라스의 정리를 활용하여 원의 방정식 유도

T = int(input())

for i in range(T):
    start_x, start_y, end_x, end_y = map(int, input().split())
    planet = int(input())
    count = 0
    for j in range(planet):
        planet_x, planet_y, planet_r = map(int, input().split())
        
        # 만약 출발점과 도착점이 같은 행성 내에 있다면, 입출력이 0이다.
        if ((planet_x - start_x)**2) + ((planet_y - start_y)**2) < (planet_r ** 2) and ((planet_x - end_x)**2) + ((planet_y - end_y)**2) < (planet_r ** 2): 
            continue
        
        if ((planet_x - start_x)**2) + ((planet_y - start_y)**2) < (planet_r ** 2):
            count += 1
            
        elif ((planet_x - end_x)**2) + ((planet_y - end_y)**2) < (planet_r ** 2):
            count += 1
           
    print(count)
    
    
    
