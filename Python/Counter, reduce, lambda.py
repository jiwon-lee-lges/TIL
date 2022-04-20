def solution(clothes):
    from collections import Counter
    from functools import reduce
    
    cnt = Counter([type for name, type in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    
    return answer

### Counter -> 리스트에서 지정한 값이 등장하는 빈도 수를 key-value 형식으로 담음
### reduce(lambda~) -> 순회하면서 값을 지정한 로직에 누적적으로 적용함, 초기 값 지정 가능
### x*(y+1) - 1 -> (x+1)*(y+1) - 1 -> xy + x + y -> 옷을 매칭할 수 있는 경우의 수
