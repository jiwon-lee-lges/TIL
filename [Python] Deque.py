def solution(priorities, location):
    answer = 0
    from collections import deque
    # deque는 양방향 push/pop을 지원하며, 속도가 압도적으로 빠름
    d = deque([(v, i) for i, v in enumerate(priorities)])
    
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item) # 우선순위가 더 높은 것이 있으면 대기목록 맨 뒤로 보냄
        else:
            answer += 1 # 지금까지 인쇄된 문서의 개수
            if item[1] == location: # 인쇄를 요청한 문서가 제일 처음에 있고, 나머지 대기열 중에 우선순위가 제일 높은 경우
                break
                
    return answer
