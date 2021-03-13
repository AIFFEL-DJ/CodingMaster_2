def solution(citations: list):
    answer = 0
    count = 0
    for n in range(len(citations) + 1, 0, -1):
        for c in citations:
            if c >= n:
                count += 1
            if count >= n:
                return n
        count = 0
    return answer


print(solution([3, 0, 6, 1, 5]))
