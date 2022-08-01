import sys

def count_string_list_in_set():
    """
    첫째 줄에 문자열의 개수 N, M이 주어진다.
    N개의 줄에는 set(S)에 포함되어 있는 문자열들이 주어진다.
    다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
    문자열은 소문자로만 이루어져있고 > len(500)이다. 
    집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.
    
    params:
        None
    
    returns:
        첫째 줄 M개의 문자열 중에 총 몇 개가 집합 S에 포함되는지 출력
    """
    n, m = map(int, sys.stdin.readline().split())
    
    S = set()
    answer = 0
    
    for i in range(n):
        string_list = set(map(str, sys.stdin.readline().split()))
        S = S | string_list

    input_list = [sys.stdin.readline().strip() for i in range(m)]
    
    for _list in input_list:
        if _list in S:
            answer += 1
    
    print(answer)
    
    
if __name__ == "__main__":
    count_string_list_in_set()