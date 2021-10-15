N, S = input().split()
N, S = int(N), int(S)
A = list(map(int, input().split()))
B = A.copy()
B[S - 1] = -1
print(B)

right = 0
left = 0
visited = 2
total = A[S - 1]
current = S

while visited <= N:
    if S + right + 1 > N:
        left += 1
        current = S - left
    elif S - left - 1 < 1:
        right += 1
        current = S + right
    else:
        if B.index(max(B)) > current - 1:  # A[S + right] > A[S - left - 2]:
            right += 1
            current = S + right
        else:
            left += 1
            current = S - left
        if current-1 == B.index(max(B)):
            B[current-1] = -1
    total += A[current - 1] * visited
    visited += 1

print(total)
