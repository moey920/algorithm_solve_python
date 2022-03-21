import sys
from itertools import permutations


def n_m_sequence():
    """
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    itertools.permutations 메서드를 활용하여 
    중복을 허용하지 않고 순서가 의미를 가진 순열을 구한다.
    
    params:
        None
    
    returns:
        한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
        중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
        수열은 사전 순으로 증가하는 순서로 출력해야 한다.
    """
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    n_list = [i for i in range(1, n+1)]
    
    # permutations(iterable객체, r)
    cnt = 0
    for i in permutations(n_list, m):
        print(' '.join(map(str, i)))
            
            
if __name__ == "__main__":
    n_m_sequence()