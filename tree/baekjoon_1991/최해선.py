import sys
n = int(sys.stdin.readline())
tree = {}
root = None
for i in range(n):
    parent,left,right = sys.stdin.readline().split()
    if root ==None:
        root = parent
        tree[root] = left,right
    else:
        tree[parent] = left,right
def pre(root):
    if root != '.':
        print(root,end='')
        pre(tree[root][0])
        pre(tree[root][1])
def in_(root):
    if root != '.':
        in_(tree[root][0])
        print(root,end='')
        in_(tree[root][1])
def post(root):
    if root != '.':
        post(tree[root][0])
        post(tree[root][1])
        print(root,end='')
pre(root)
print('')
in_(root)
print('')
post(root)
# def presearch(root): 
#     # if root != '.':
#     # print(root)
#     answer = ''
#     answer += root
#     temp = [] # 부모저장용
#     temp.append(root)
#     umbba = root
#     while True:
#         if tree[umbba][0] != '.':
#             answer += tree[umbba][0]
#             temp.append(tree[umbba][0])
#             umbba = tree[umbba][0]            
#         elif tree[umbba][1] != '.':
#             answer += tree[umbba][1]
#             temp.append(tree[umbba][1])
#             umbba = tree[umbba][1]
#         while True:
#             if tree[temp[-1]][1] != ".":
#                 temp.pop()
#             else:
#                 umbba = tree[temp[-1]][1]
#                 break    
