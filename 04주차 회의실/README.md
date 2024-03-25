> 마크다운 사용법 링크: https://gist.github.com/ihoneymon/652be052a0727ad59601

## 1. 교수님의 수업 내용 정리!
  ```
  1. 파이썬의 int, big int(long long) 처리와 ALU의 동작:
      1.1.  x32(int) 1e9 -> BCD 방식으로 더 적은 비트 이용
            1e9를 넘는 건 lossless -> 문자열로 변경
            예) ("1, 2, 1, 2, 4, ...") -> Mod 계산하려면 해당 원소 찾기 (O(logN)) + 아스키코드로 정수 변환 + MOD연산
            => 즉, Mod 연산이 ALU(산술논리연산장치)의 사용만으로는 부족하고 그 외의 여러 자원이 쓰인다.
      1.2.  x64(long long) 1e19 -> 크기를 넘는 건 여러 bit를 써서 표현
            예) (x64, x63) -> 이런식으로 비트 2개를 붙임.
            => ALU의 사용만으로 Mod 연산 수행 가능

  2. packing, unpacking 개념:
      - packing: 각각의 객체를 튜플에 하나로 합쳐준다.
      - unpacking: 튜플의 객체를 분리해서 하나의 객체로 만들어준다.
      예) a, b = a+b, a-b
         (left)  (right)
      2.1.  right에 있는 식부터 계산을 한다.
      2.2.  (a, b) = (상수, 상수) -> ',' 로 구분되는 것은 튜플이기에 unpacking 개념이 쓰임.
      예2) 함수 인자 여러개를 입력받아야 하는 경우:
      - 원래:
        a, b, c = map(int, input().split())
        func(a, b, c): ...
      - unpacking 적용:
        func(*map(int, input().split()) => 입력 받는 객체들을 분리해서 넣어줌.

  3. 내장 라이브러리 heapq:
      3.1.  import heapq
            heapq.heappush(arr, x) => 배열 arr에 x를 append해라.
            해당 라이브러리 내장 함수에 heapq 원리 구현됨. => 보는 법: import heapq 라이브러리를 [Ctrl] + 클릭


  4. Queue vs Deque(뎈) vs Priority Queue vs Indexed Priority Queue:
      4.1.  Queue (First in first out)
              __________
            <-__________ <-
      4.2.  Deque (양 방향 push&pop 가능)
              __________
            <->________<->
      4.3.  PQ (무조건 가장 작은 값을 pop)
              __________
            <-(vip!)ooo <-
              __________
      4.4.  IPQ (각 원소의 위치를 기록한 배열을 생성) : O(N) x O(logN) + 2 여기서 O(N)를 없애겠다는 목표
  ```

 
## 숙제
|난이도|번호|제목|링크|
|-|-|-|-|
| S3 | 1788번 | 피보나치 수의 확장| https://www.acmicpc.net/problem/1788 |
| G3 | 19623번 |  회의실 배정 4 | https://www.acmicpc.net/problem/19623 |

## 찾아온 문제들
#### 민기홍
|난이도|번호|제목|링크|
|-----|-----|---------------------|----------------------------------------|
| G3 | 2143번 | 두 배열의 합 | https://www.acmicpc.net/problem/2143 |

#### 김동주
|난이도|번호|제목|링크|
|-----|-----|---------------------|----------------------------------------|
| G5 |12731번|열차 시간표(Small)|https://www.acmicpc.net/problem/12731 |

#### 정우현
|난이도|번호|제목|링크|
|-----|-----|---------------------|----------------------------------------|
|골드 4|번||https://www.acmicpc.net/problem/|
|골드 5|번||https://www.acmicpc.net/problem/|

#### 서동혁
|난이도|번호|제목|링크|
|-----|-----|---------------------|----------------------------------------|
|실버 2|1927번|최소 힙|https://www.acmicpc.net/problem/1927|
