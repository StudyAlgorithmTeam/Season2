# 영재의 시험


from functools import cache


N = 10
K = 5
ANSWERS = [*map(int, input().split())]


@cache
def solve(i = 0, ans_1 = None, ans_2 = None) -> tuple:
    cases = [0] * (N+1)
    if i == 10:
        cases[0] = 1
    else:
        for ans_0 in range(1, 6):
            is_ans = bool(ans_0 == ANSWERS[i])
            if ans_0 == ans_1 == ans_2:
                continue
            for n_ans, n_cases in enumerate(solve(i+1, ans_0, ans_1)):
                if is_ans and n_ans < N:
                    n_ans += 1
                cases[n_ans] += n_cases
    return cases


if __name__ == '__main__':
    print(sum(solve()[K:]))
