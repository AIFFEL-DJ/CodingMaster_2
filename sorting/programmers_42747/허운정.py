def solution(citations):
  citations.sort()
  h = 0; k = 0; answer = 0
  for i in range(0, citations[-1]+1):
    h = sum(j>=i for j in citations) # i번 이상 인용된 논문수인 h를 구함
    k = sum(j<=i for j in citations) # i번 이하 인용된 논문수인 k를 구함
    if h >= i and k <= i: #h가 i 이상이고 k가 i 이하인 조건을 만족하는 값을 구함
      if i > answer : answer = i #그중에 최대값을 구함
  if citations[0] >= len(citations): answer = len(citations)
  return answer
