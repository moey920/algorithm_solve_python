def num_of_six():
    """
    1의 자리수부터 검사해서 최소한의 n의 자리수에 6이 3개 이상 포함되어 있으면 리스트에 쌓는다.
    input:
        N: 결과의 N번째 원소

    return:
        연속된 666이 포함된 수 중 N번째로 작은 수
    """
    N = int(input())
    result = []
    i = 0

    while len(result) != N:
        if list(str(i)).count('6') >= 3:
            if '666' in str(i):
                result.append(i)
        i += 1
    print(result[N - 1])


if __name__ == "__main__":
    num_of_six()
