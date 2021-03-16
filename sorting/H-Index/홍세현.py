def solution(citations):

    citations = sorted(citations)
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i
