expression = input()

left = []
right = []
isLeft = False

for (pos, char) in enumerate(list(expression)):
    isLeft = len(left) - len(right) > 0
    if char == '(':
        left.insert(len(left) if not isLeft else len(left) - 1, pos + 1)
    elif char == ')':
        right.append(pos + 1)
    else:
        continue

print(len(right))
for l, r in zip(left, right):
    print(l, r)
