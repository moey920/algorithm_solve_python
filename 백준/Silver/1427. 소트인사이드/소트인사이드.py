import sys

def sort_digit(N):
    """
    수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬한다.

    :param N:
        문자열 N을 받는다.
    :return:
        자연수 N의 각 자리수를 내림차순으로 정렬하여 자연수로 반환한다.
    """
    n_list = [i for i in N]
    print(int(''.join(sorted(n_list, reverse=True))))


if __name__ == "__main__":
    input = sys.stdin.readline
    N = input().strip()
    sort_digit(N)