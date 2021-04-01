import sys

def main():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        
        s, t = line.split()

        ps, pt = 0, 0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1

        if ps == len(s):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()