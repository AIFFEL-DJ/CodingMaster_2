def solution(citations: list):
    answer = 0
    count = 0
    for h in range(len(citations) + 1, 0, -1):
        for c in citations:
            if c >= h:
                count += 1
            if count >= h:
                return h
        count = 0
    return answer


print(solution([3, 0, 6, 1, 5]))
