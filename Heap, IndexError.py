def solution(scoville, K):
    answer = 0
    
    import heapq
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            scv = first + (second * 2)
            heapq.heappush(scoville, scv)
            
        except IndexError: # 주어진 원소로 K이상의 스코빌 지수를 만들 수 없는 경우 
            return -1
        answer += 1
    
    return answer
  
  ### heap 자료형은 min/max를 더 효울적으로 찾을 수 있도록 만들어짐
  ### 주어진 scoville 리스트를 heapq모듈로 heap 자료형으로 만들고, heap[0] (최솟값)이 K 이상이 될 때까지 (변형이 완료될 때까지) 스코빌 지수 변환을 수행해 다시 push함
  ### 스코빌 변환을 계속 반복해 힙 안에 원소가 1개 밖에 안 남았는데도 주어진 K보다 값이 작다면 K를 만들 수 없는 경우로, heappop을 할 때 IndexError가 발생하므로 try-except문을 사용해 에러를 잡아줌
