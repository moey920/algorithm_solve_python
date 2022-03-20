import sys
from collections import Counter

def statistics(N):
    """
    산술평균 : N개의 수들의 합을 N으로 나눈 값
    중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    최빈값 : N개의 수들 중 가장 많이 나타나는 값
    범위 : N개의 수들 중 최댓값과 최솟값의 차이

    :param N: N개의 수를 입력받는다.
    :return: 산술평균, 중앙값, 최빈값, 범위(최댓값-최솟값)를 리턴한다.
    """
    num_list = [int(input()) for i in range(N)]

    # 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    print(round(sum(num_list) / N))

    # 중앙값을 출력한다.
    print(sorted(num_list)[len(num_list) // 2])

    # 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    cnt_dict = Counter(sorted(num_list)).most_common()
    if len(cnt_dict) > 1 and cnt_dict[0][1] == cnt_dict[1][1]:
        print(cnt_dict[1][0])
    else:
        print(cnt_dict[0][0])

    # N개의 수들 중 최댓값과 최솟값의 차이
    print(sorted(num_list)[-1] - sorted(num_list)[0])


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    statistics(N)
