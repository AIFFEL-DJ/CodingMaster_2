sentence = input()

s, t = sentence.split()

j = 0
word = ''

for i in range(len(t)):
    if t[i] == s[j]:
        word += t[i]
        j += 1
        if j==len(s):
            break
    
if s in word:
    print("Yes")
else:
    print("No")
