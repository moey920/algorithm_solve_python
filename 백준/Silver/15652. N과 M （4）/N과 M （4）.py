import sys


def combinations_with_replacement(n, m, s, cnt):
    """
    1부터 N까지 자연수 중에서 M개를 고른 수열(중복 조합, combinations_with_replacement)
    같은 수를 여러 번 골라도 된다.
    고른 수열은 비내림차순이어야 한다.
    itertools.combinations_with_replacement(iterable객체, r)로 쉽게 구할 수 있으나,
    백트래킹 문제 의도에 맞게 백트래킹을 활용해 풀이해본다.
    
    params:
        n : 1부터 n까지의 자연수
        m : 중복이 없는 m개
        s : 빈 리스트
    
    returns:
        중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
        수열은 사전 순으로 증가하는 순서로 출력해야 한다.
    """
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(cnt, n+1):
        combinations_with_replacement(n, m, s + [i], cnt)
        cnt += 1
        
            
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    s = []
    combinations_with_replacement(n, m, s, 1)