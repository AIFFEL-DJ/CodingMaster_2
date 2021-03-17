def solution(citations):
    answer = 0
    citations.sort()
    index = []
    for i in range(0,len(citations)+1):
        n = 0
        for j in citations:
            if j >= i:
                n += 1
                
        index.append(n)

        if index[i] >= i:
            answer = i
        else:
            break

    return answer
