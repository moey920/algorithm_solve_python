import sys
from collections import OrderedDict

def sort_str(N):
    """

    :param N:
        정렬 할 문자열의 개수 N

    :return:
        N개의 문자열을 문자열 길이 순서대로, 길이가 같으면 사전 순으로 정렬한다.
    """

    str_list = [input().strip() for _ in range(N)]
    str_list.sort()
    str_list.sort(key=lambda x: len(x))
    for _str in list(OrderedDict.fromkeys(str_list)):
        print(_str)


if __name__ == "__main__":
    _input = sys.stdin.readline
    N = int(_input())
    sort_str(N)