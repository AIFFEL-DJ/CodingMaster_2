def main():
    n, k = map(int, input().split())
    circular_list = []
    for i in range(1, n+1):
        circular_list.append(i)

    pop_idx = 0
    answer = []
    while len(circular_list) > 0:
        pop_idx = (pop_idx + k - 1) % len(circular_list)
        elem = circular_list.pop(pop_idx)
        answer.append(elem)
        
    print("<", end='')
    print(*answer, sep=", ", end='')
    print(">")


if __name__ == "__main__":
    main()