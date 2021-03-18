"""
프로그래머스 - H-Index
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면 h의 최대가 이 과학자의 H-Index입니다.       

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

wiki에서의 정의 
H-Index = maxmin(f(i), i) # f(i)=i번째 논문의 인용 횟수 

[3, 0, 6, 1, 5]	=> 3번
[20, 19, 18, 1] => 3번 
[22, 42] => 2번 
<=> h index 개수 이상 인용된 논문의 h index 개수 
min"""

# 어려워서 정답보고 공부했습니다
def solution(citations):
    citations.sort(reverse = True) # 내림차순으로 정렬 
    answer = max(map(min, enumerate(citations, start=1))) 
    # (1, citations[0]), citations[0]은 가장 큰 인용 횟수
    # (2, citations[1])
    # ... 
    # (n, citations[n-1]), citations[n-1]은 가장 적은 인용 횟수

    # min으로 mapping되면, 두 데이터 중 최소만 취함
    # 그 중 max로 취함 
    return answer