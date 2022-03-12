def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] > 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            
    answer.append(count)
    return answer
  
  ### 마지막 프로세스까지 신경써줘야 함
  ### While 문이 len(progresses) > 0 까지 돌기 때문에 마지막 count는 answer에 한 번 더 append해야 함
