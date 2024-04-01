from sys import stdin
from sys import stdout


def testcase(tid):
    word = stdin.readline().strip()
    stdout.write(min(make_words(word)))
    stdout.write('\n')


def make_words(word):
    n = len(word)
    for pivot1 in range(n-2):
        for pivot2 in range(pivot1+1, n-1):
            yield word[pivot1::-1] + word[pivot2:pivot1:-1] + word[:pivot2:-1]


if __name__ == '__main__':
    # setrecursionlimit(int(1e6))
    # T = int(stdin.readline())
    # for tid in range(1, T+1):
    #     testcase(tid)
    testcase(0)
