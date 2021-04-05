import sys

for order in sys.stdin.read().splitlines():
    N, K = map(int, order.split())
    i = 0
    input_list = list(range(1, N + 1))
    output_list = []

    while input_list:
        i = (i + K - 1) % len(input_list)
        output_list.append(input_list.pop(i))

    print(f"<{', '.join(map(str, output_list))}>")
