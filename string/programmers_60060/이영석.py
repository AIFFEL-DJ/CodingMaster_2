# 정확성 테스트는 모두 통과
# 효율성 테스트는 4, 5만 통과 (나머지는 시간초과)

def solution(words, queries):
    answer = [0] * len(queries)
    
    for idx, q in enumerate(queries):
        for w in words:
            word_len = len(w)
            if len(q) != word_len:
                continue
            if q[0] == '?' and q[-1] == '?':
                answer[idx] += 1
                continue

            quest_mark_idx = q.find('?')
            if quest_mark_idx != 0:
                # Ex) "fro??"
                if w[:quest_mark_idx] == q[:quest_mark_idx]:
                    answer[idx] += 1
            else:
                # Ex) "????o"
                quest_mark_idx = q[::-1].find('?')
                if w[word_len - quest_mark_idx:] == q[word_len - quest_mark_idx:]:
                    answer[idx] += 1

    return answer