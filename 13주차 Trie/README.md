> [마크다운 사용법 - 참고 링크](https://gist.github.com/ihoneymon/652be052a0727ad59601)

## 숙제

| 난이도 | 번호  | 제목        | 링크                 |
| ------ | ----- | ----------- | -------------------- |
| ![S1]  | 1141  | 접두사      | https://boj.kr/1141  |
| ![S1]  | 14426 | 접두사 찾기 | https://boj.kr/14426 |

## 스터디 내용

<https://namu.wiki/w/트라이>

<details><summary>C 코드 보기</summary>

```c
#include <stdbool.h>
#include <stdlib.h>


typedef struct node {
    bool is_end;
    struct node* child[26];
} node;


void make_trie(node* node, char* str) {
    char c = str[0];
    int index = c - 'a';

    if (c == '\0') {
        node->is_end = true;
        return;
    }

    struct node *child = node->child[index];

    if (child == NULL) {
        child = (struct node*) malloc(sizeof(struct node));
        child->is_end = false;
        node->child[index] = child;
    }

    make_trie(child, str + 1);
}

int count(node* node) {
    int cnt = 0;
    for (int i = 0; i < 26; i++) {
        if (node->child[i] != NULL) {
            cnt += count(node->child[i]);
        }
    }
    if (cnt == 0) {
        cnt++; // leaf node
    }
    return cnt;
}

int main() {
    node* root = (node*) malloc(sizeof(node));
    root->is_end = false;

    int N;
    char word[51];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%s", word);
        make_trie(root, word);
    }
    count(root);

    return 0;
}
```

</details>

<details><summary>Python 코드 보기</summary>

```python
import sys
# from collections import defaultdict


class Trie:
    def __init__(self) -> None:
        # self.children = defaultdict(Trie)
        self.children = {}
        self.is_end = False

    def make(self, word: str):
        if len(word) == 0:
            self.is_end = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].make(word[1:])

    def count(self):
        if self.is_leaf():
            return 1
        return sum([child.count() for child in self.children.values()])

    def is_leaf(self) -> bool:
        return len(self.children) == 0


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    root = Trie()
    for i in range(N):
        word = sys.stdin.readline().strip()
        root.make(word)
    print(root.count())
```

</details>

## 찾아온 문제들

#### 김동주

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 정우현

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 서동혁

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 손영준

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

<!-- 문제 템플릿

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

-->

<!-- solved.ac 문제 난이도 별 태그 이미지 -->

[P1]: https://d2gd6pc034wcta.cloudfront.net/tier/20.svg
[P2]: https://d2gd6pc034wcta.cloudfront.net/tier/19.svg
[P3]: https://d2gd6pc034wcta.cloudfront.net/tier/18.svg
[P4]: https://d2gd6pc034wcta.cloudfront.net/tier/17.svg
[P5]: https://d2gd6pc034wcta.cloudfront.net/tier/16.svg
[G1]: https://d2gd6pc034wcta.cloudfront.net/tier/15.svg
[G2]: https://d2gd6pc034wcta.cloudfront.net/tier/14.svg
[G3]: https://d2gd6pc034wcta.cloudfront.net/tier/13.svg
[G4]: https://d2gd6pc034wcta.cloudfront.net/tier/12.svg
[G5]: https://d2gd6pc034wcta.cloudfront.net/tier/11.svg
[S1]: https://d2gd6pc034wcta.cloudfront.net/tier/10.svg
[S2]: https://d2gd6pc034wcta.cloudfront.net/tier/9.svg
[S3]: https://d2gd6pc034wcta.cloudfront.net/tier/8.svg
[S4]: https://d2gd6pc034wcta.cloudfront.net/tier/7.svg
[S5]: https://d2gd6pc034wcta.cloudfront.net/tier/6.svg
[??]: https://d2gd6pc034wcta.cloudfront.net/tier/0.svg
