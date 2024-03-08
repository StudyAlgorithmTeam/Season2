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


def dh(S):
    pelin = int(S)
    pelin = pelin + 1
    #1을 더하고 시작하면 홀 짝이 확실히 정해지고 시작 ex)9999
    str_pel = str(pelin)

    list1 = list(map(int,list(str(pelin))))
    num = len(list1)

    if(len(list1) % 2 == 0):
        front = str_pel[0:int((num/2))]
        rev_front = int(front[::-1])
        back = int(str_pel[int(num/2):])
        if(rev_front >= back):
            return int(front + str(rev_front + 1))
        else:
            temp_front = int(front)+1
            temp_rev_front = int(str(temp_front)[::-1])
            return int(str(temp_front) + str(temp_rev_front))
    else:
        front = str_pel[0:int((num-1)/2)]
        rev_front = int(front[::-1])
        back = int(str_pel[int((num-1)/2)+1:])
        if(rev_front < back):
            if(list1[int((num-1)/2)]==9):
                temp_front = int(front) + 1
                temp_rev_front = int(str(temp_front)[::-1])
                list1[int((num-1)/2)] = 0
                return int(str(temp_front) + '0' + str(temp_rev_front))
            else:
                list1[int((num-1)/2)] = list1[int((num-1)/2)] + 1
                return int(front + str(list1[int((num-1)/2)]) + str(rev_front))
        elif(rev_front >= back):
            return int(front + str(list1[int((num-1)/2)]) + str(rev_front))

if __name__ == "__main__":
    for i in range(10, 10**50):
        s = str(i)
        if str(main(s)).strip() != str(dh(s)).strip():
            print(s, str(main(s)).strip(), str(dh(s)).strip())
            input()
