import sys
n_iter = list(sys.stdin.readline().split())

test = []
for i in range(0,len(n_iter),2):
    test.append([n_iter[i],n_iter[i+1]])

def solution(s,t):
    tem = 0
    for i in range(len(t)):
        if t[i] == s[tem]:
            tem += 1
            if len(s) == tem:
                return 'Yes'
    return 'No'
for i in test:
    print(solution(i[0],i[1]))
