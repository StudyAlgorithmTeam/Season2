# 알프수


X = list(map(int, input().strip()))
is_alpsoo = False
if X[0] < X[1] and X[-2] > X[-1]:
    for i in range(2, len(X)):
        prev_diff = X[i-2] - X[i-1]
        curr_diff = X[i-1] - X[i]
        is_alpsoo = (prev_diff == curr_diff) or (prev_diff * curr_diff < 0)
        if not is_alpsoo:
            break
if is_alpsoo:
    print('ALPSOO')
else:
    print('NON ALPSOO')
