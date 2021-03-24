def substring():
    s, t = input().split()
    check = 0
    
    for i in range(len(t)):
        if t[i] == s[check]:
            check += 1
            if check == len(s):
                return 'Yes'
            
    return 'No'



s, t = input().split()
check = 0

for i in range(len(t)):
    if t[i] == s[check]:
        check += 1
        if check == len(s):
            print('Yes')
            break

if check != len(s):            
    print('No')        
