import typing


def main(s: str) -> str:
    number = str(int(s)+1)
    numbers = list(map(int, number))
    make_palindrome(numbers)
    return ''.join(map(str, numbers))


def make_palindrome(numbers: typing.List[int], s: int = 0, e: int = None, increased_at: int = None):
    if e is None:
        e = len(numbers) - 1
    if increased_at is None:
        increased_at = len(numbers)

    if s > e:
        # 모든 수를 완성했다는 뜻.
        return

    if numbers[s] < numbers[e]:
        if increased_at >= e:
            # e번째 자리 수 이전에 증가된 숫자가 없을 경우에는 숫자를 낮출 수 없다.
            # 따라서, 앞자리 수에서 값을 증가시킨 뒤, e번째 숫자를 낮춘다.
            increased_at = increase_a_bit(numbers, s, e)

    numbers[e] = numbers[s]

    make_palindrome(numbers, s+1, e-1, increased_at)



def increase_a_bit(numbers: typing.List[int], s: int, e: int) -> int:
    """[s, e) 구간에서 증가 시킬 수 있는 수 중 가장 작은 숫자를 증가시킴.

    증가시킨 수의 인덱스를 반환한다.
    """
    for i in range(e-1, s-1, -1):
        if numbers[i] != 9:
            numbers[i] += 1
            # 증가시킨 이후의 숫자는 가장 작은 수(=0)로 맞춰주자.
            for j in range(i+1, e):
                numbers[j] = 0
            return i
    raise ValueError('omg 증가를 시킬 숫자가 없다!!!')



if __name__ == "__main__":
    # print(main("12345"), 12421)
    # print(main("858"), 868)
    # print(main("1999"), 2002)
    # print(main("1"), 2)
    # print(main("9999"), 10001)
    # print(main("4995"), 5005)
    # print(main("498"), 505)
    # print(main("10001"), 10101)
    # print(main("5749201"), 5749475)
    # print(main("12012"), 12021)
    # print(main("110101"), 111111)
    # print(main("4651354631683213233486146513546316832132334861"), "시간 초과 검사용")
    print(main(input()))
