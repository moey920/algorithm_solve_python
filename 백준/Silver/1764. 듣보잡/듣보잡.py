import sys

def get_unknown_name():
    """
    정수 N과 M을 한줄에 입력받고
    N과 M개의 문자열을 한 줄씩 입력받아
    N과 M이 겹치는 경우의 수와, 그 문자열을 사전순으로 출력한다.
    
    Args:
        None
    
    Returns:
        None
    """
    input = sys.stdin.readline
    never_heard_name = set()
    never_seen_name = set()
    n, m = map(int, input().split())
    for _ in range(n):
        never_heard_name.add(input())
    for _ in range(m):
        never_seen_name.add(input())
    
    unknown_name = never_heard_name & never_seen_name
    print(len(unknown_name))
    sorted_unknown_name = sorted(list(unknown_name))
    for name in sorted_unknown_name:
        print(name, end='')

if __name__ == "__main__":
    get_unknown_name()