import sys

def sort_age():
    """
    값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬(stable sort)이라고 합니다.
    
    :param:
        회원의 수 n
        
    :return:
        첫째 줄부터 총 N개의 줄에 걸쳐 회원을 나이 순,
        나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력
    """
    _input = sys.stdin.readline
    n = int(_input())
    member_list = [list(map(str, _input().split())) for _ in range(n)]
    member_list.sort(key=lambda x: int(x[0]))

    for member in member_list:
        print(member[0], member[1])

if __name__ == "__main__":
    sort_age()