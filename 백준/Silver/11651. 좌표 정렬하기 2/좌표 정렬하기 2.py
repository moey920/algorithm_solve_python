import sys

def sort_coordinate(N):
    """
    N개의 좌표를 정렬하여 반환합니다.

    :param N:
        정렬 할 좌표의 개수 N

    :return:
        Yn이 큰 순서대로, Yn이 같다면 Xn이 큰 순서대로 좌표를 정렬하여 반환
    """
    coordinate_list = [list(map(int, input().split())) for _ in range(N)]
    coordinate_list.sort(key=lambda x: (x[1], x[0]))

    for i in coordinate_list:
        print(i[0], i[1])


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    sort_coordinate(N)