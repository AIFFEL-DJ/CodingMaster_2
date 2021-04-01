N,K = map(int,input().split())
round_list = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들
answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1 #pop를 하면서 길이가 짧아짐에 따라 인덱스도 짧아져야함 
    # print(num,len(round_list))  
    if num >= len(round_list):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(round_list)
 
    answer.append(str(round_list.pop(num)))
print("<",", ".join(answer)[:],">", sep='')
