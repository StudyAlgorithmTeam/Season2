def main(S: str) -> int:
    # O(N^2)
    for s in range(len(S)):
        # s 번째 원소부터 마지막 글자까지 팰린드롬인지 본다.
        if is_palindrome(S, s, len(S)-1):
            # [0,s) 구간의 문자 s개를 뒤집어서 S의 뒤에 붙여주면 팰린드롬이 된다.
            return len(S) + s
    # `s`가 `len(S)-1`과 같은 길이 1의 문자열이면 무조건 팰린드롬일 텐데,
    # 여기까지 프로그램이 도달했다는 건 분명 내 코드에 논리적인 문제가 있는 것이다.
    raise ArithmeticError


def is_palindrome(string: str, start: int, end: int):
    # 문자열이 좌우 대칭인지 검사. O(N)
    for offset in range((end-start+1)//2):
        if string[start+offset] != string[end-offset]:
            return False
    return True


if __name__ == "__main__":
    # print(main("abab"), 5)
    # print(main("abacaba"), 7)
    # print(main("qwerty"), 11)
    # print(main("abdfhdyrbdbsdfghjkllkjhgfds"), 38)
    print(main(input()))
