def bad_example(fwd, bwd, s):
    dist = (fwd-bwd) * (s//(fwd+bwd)) # dist so far
    rem = s % (fwd+bwd) # dist remains
    if rem <= fwd:
        dist += rem
    else:
        dist -= rem - fwd
    return dist


def good_example(fwd, bwd, s):
    dist = (fwd-bwd) * (s//(fwd+bwd)) # dist so far
    rem = s % (fwd+bwd) # dist remains
    if rem <= fwd:
        dist += rem
    else:
        dist += fwd-(rem-fwd)
    return dist


def select_winner(nikky, byron):
    if nikky > byron:
        return 'Nikky'
    elif nikky < byron:
        return 'Byron'
    else:
        return 'Tied'


def find_counter_example():
    # 문제에서 a >= b, c >= d 를 보장한다:
    for d in range(1, 101):
        for c in range(d, 101):
            for b in range(1, 101):
                for a in range(b, 101):
                    for s in range(1, 10001):
                        if select_winner(good_example(a, b, s), good_example(c, d, s)) != select_winner(bad_example(a, b, s), bad_example(c, d, s)):
                            print('Case Found:')
                            print(a)
                            print(b)
                            print(c)
                            print(d)
                            print(s)
                            print()
                            return


find_counter_example()
