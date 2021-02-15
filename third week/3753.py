N, M = map(int, input().split())

A = {int(input()) for _ in range(N)}

B = {int(input()) for _ in range(M)}

for S in [A & B, A - B, B - A]:

    print(len(S))

    print(*sorted(S))