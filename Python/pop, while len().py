def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = [0] * bridge_length
    
    while len(truck):
        answer += 1
        truck.pop(0)
        if truck_weights:
            if truck_weights[0] + sum(truck) <= weight:
                truck.append(truck_weights.pop(0))
            else:
                truck.append(0)
        
    return answer

### if-else 문에 중복된 동작은 밖으로 끌어내 한 번만 기술해도 됨
### while len(truck) -> truck에 있는 원소들이 모두 없어질 때까지 (길이가 0이 될 때까지) 반복됨
### pop(0) v.s. pop() -> pop(0)은 리스트 인덱스 0부터 뽑고, pop()은 맨 마지막부터 뽑음
