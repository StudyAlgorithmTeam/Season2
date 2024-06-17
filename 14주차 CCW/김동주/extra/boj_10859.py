# 뒤집어진 소수


def is_prime_str(s: str) -> bool:
    n = int(s)
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def flip_str(s: str) -> str:
    return ''.join(reversed([*map(flip_chr, s)]))


def flip_chr(c: str) -> str:
    if c in '6':
        return '9'
    if c in '9':
        return '6'
    if c in '347':
        raise ValueError
    return c


if __name__ == "__main__":
    N = input().strip()
    try:
        assert is_prime_str(N)
        assert is_prime_str(flip_str(N))
        print('yes')
    except (ValueError, AssertionError):
        print('no')
