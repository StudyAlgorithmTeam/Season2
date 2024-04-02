from sys import stdin


N = 10
INF = 1000
RAW_BULB_ON = 'O'
RAW_BULB_OFF = '#'


def grid_encode(lines):
    hash = 0
    for y in range(N):
        hash <<= 2
        for x in range(N):
            hash <<= 1
            if lines[y][x] == RAW_BULB_ON:
                hash |= 1
    return hash


def grid_decode(hash):
    lines = [[RAW_BULB_OFF]*N for y in range(N)]
    for y in reversed(range(N)):
        for x in range(N):
            if hash & (1 << (N-x-1)):
                lines[y][x] = RAW_BULB_ON
        hash >>= N+2
        lines[y] = ''.join(lines[y])
    return lines


def init_kernel():
    kernel = 0
    kernel = (kernel << (N+2)) | 0b0100000000
    kernel = (kernel << (N+2)) | 0b1110000000
    kernel = (kernel << (N+2)) | 0b0100000000
    kernel = kernel << ((N+2) * (N-3))
    kernel_topleft_mask = 1
    kernel_topleft_mask <<= (N+2)*(N-1)+N-1

    # 커널의 중심이 그리드의 좌상단에 위치하도록 옮김
    kernel <<= (N+2)+1
    kernel_topleft_mask <<= (N+2)+1
    kernel_center_mask = kernel_topleft_mask >> ((N+2)+1)

    kernel_mask = 0
    for y in range(N):
        kernel_mask <<= N+2
        kernel_mask |= 0b1111111111

    return kernel, kernel_mask, kernel_center_mask


def bruteforce(grid, kernel, kernel_mask, kernel_center_mask):
    # 첫 번째 행에 대해서는 완전탐색 O(2^N)
    for i in range(1 << N+1):
        g = grid
        k = kernel
        n_xors = 0
        for x in range(N):
            if i & (1 << x):
                g ^= k
                n_xors += 1
            k >>= 1
        yield n_xors + bruteforce_downward(g, kernel, kernel_mask, kernel_center_mask)


def bruteforce_downward(grid, kernel, kernel_mask, kernel_center_mask):
    # 두 번째 행 이후로는 그리디로, 그냥 켜진 것만 끔 O(N^2)
    n_xors = 0
    kernel >>= (N+2)
    kernel_center_mask >>= (N+2)
    while kernel_center_mask:
        # 누를 수 있는 버튼일 때만 누른다
        if kernel_center_mask & kernel_mask:
            kernel_top_mask = kernel_center_mask << (N+2)
            if grid & kernel_top_mask:
                grid ^= kernel
                n_xors += 1
        kernel >>= 1
        kernel_center_mask >>= 1
    return INF if (grid & kernel_mask) else n_xors


if __name__ == '__main__':
    kernel, kernel_mask, kernel_center_mask = init_kernel()
    grid = grid_encode(stdin.readlines())
    n_xors = min(bruteforce(grid, kernel, kernel_mask, kernel_center_mask))
    print(-1 if n_xors == INF else n_xors)
