import numpy

N = int(input())
A = []
while len(A) != N:
    A = list(map(int, input().split()))
absA = list(map(abs, A))

addition = round(float(numpy.std(absA)) * 2) / 2.0
sumA = sum(A)
print(sum(A))
A = [i + addition if sumA > 0 else i - addition for i in A]

print(sum(A))
