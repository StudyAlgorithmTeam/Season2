"""
N과 K가 다음과 같을 때:
- N: 참가자 수
- K: 카드에 적힐 수 있는 최대 숫자

처음 나오는 for-loop 까지 O(N+K)

두 번째 for-loop에서
1. 시작할 때 sorted() 에서 O(N log N)
2. 바깥 루프는 N번 순회
3. 안쪽 루프는 최대 K번 순회 (하지만 안쪽 루프의 순회 횟수는 사실 상 점진적으로 크게 감소)

점근적 분석에 의한 시간 복잡도는 O(NK + N log N) 으로 보아야 할 것 같다.
"""

N = int(input())

player_card = [*map(int, input().split())]
player_score = [0] * N

max_card = max(player_card)
card_player_id = [None] * (max_card+1)

for player_id in range(N):
    card_player_id[player_card[player_id]] = player_id

for win_card in sorted(player_card):
    for lose_card in range(2*win_card, max_card+1, win_card):
        if card_player_id[lose_card] is not None:
            player_score[card_player_id[win_card]] += 1
            player_score[card_player_id[lose_card]] -= 1

print(' '.join(map(str, player_score)))
