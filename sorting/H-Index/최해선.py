def solution(ci):
    ci.sort(reverse= True)
    if len(ci) == 0:
        answer = 0
    else:
        for a,i in enumerate(ci):
            if i < a+1:
                answer = a
                break
            else:
                answer = len(ci)
    return answer
# []과, 같은 수 논문인용수만 있을 때도 추가하여 해결했습니다