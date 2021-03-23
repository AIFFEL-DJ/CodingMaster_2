def solution(words, queries):
    answer = []    
    for i in queries:
        con = 0
        b = i.split('?')
        bh = b[0]
        bt = b[-1]
        b = list(filter(lambda x: len(x) != 0, b))

        for j in words:
            if len(i) == len(j):
                if len(b) == 0:
                    con += 1
                elif j[:len(b[0])] == (bh):
                    con += 1
                elif j[-len(b[0]):] == (bt):
                    con += 1
        answer.append(con)          
    return answer
