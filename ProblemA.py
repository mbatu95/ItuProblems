N = input()
matches = input()
K = 0
V = 0
K_current = 0
V_current = 0

for c in list(matches):
    if c == 'K':
        K_current += 1
        if K_current > 10 and (V_current < 10 or (V_current >= 10 and K_current - V_current == 2)):
                K += 1
                K_current = V_current = 0
    else:
        V_current += 1
        if V_current > 10 and (K_current < 10 or (K_current >= 10 and V_current - K_current == 2)):
                V += 1
                K_current = V_current = 0

print(str(K) + ':' + str(V))
if K_current > 0 or V_current > 0:
    print(str(K_current) + ':' + str(V_current))
