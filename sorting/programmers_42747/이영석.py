def count_over_num(citations, num):
    count = 0
    for i in citations:
        if i >= num:
            count += 1

    if count >= num:
        return True
    return False


def solution(citations):
    n = len(citations)

    h_list = []
    for c in range(n, 0, -1):
        if count_over_num(citations, c):
            h_list.append(c)
    
    if len(h_list) == 0:
        return 0

    return max(h_list)