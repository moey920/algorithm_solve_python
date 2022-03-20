import sys


def coordinate_compression():
    """
    Xi의 좌표 압축(Xi > Xj) 결과인 리스트 X'n을 구한다.
    list.index(i) 형태의 시간 복잡도 = O(N)
    index[i] 형태의 시간 복잡도 = O(1)

    :param:
        None

    :return:
        좌표가 압축된 X'n
    """
    _input = sys.stdin.readline
    n = int(_input())
    coordinate_list = list(map(int, input().split()))

    result_list = sorted(list(set(coordinate_list)))

    result_dict = {result_list[i] : i for i in range(len(result_list))}

    for i in coordinate_list:
        print(result_dict[i], end=' ')

    # 아래 방법은 시간초과입니다.
    """
    coordinate_list = _input().split()
    result_list = [0]*len(coordinate_list)

    # coordinate_list.sort(reverse=True)
    for i in range(len(coordinate_list)):
        set_list = []
        for j in range(len(coordinate_list)):
            if int(coordinate_list[i]) > int(coordinate_list[j]):
                if int(coordinate_list[j]) in set_list:
                    pass
                else:
                    set_list.append(int(coordinate_list[j]))
                    result_list[i] += 1
    for i in result_list:
        print(i, end=' ')
    """

if __name__ == "__main__":
    coordinate_compression()
