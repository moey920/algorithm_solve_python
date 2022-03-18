def ascending_sort():
    """
    N 자리수의 숫자를 줄 별로 입력받아, 오름차순으로 정렬한 뒤 N줄로 반환합니다.
    """
    import sys
    
    input = sys.stdin.readline
    
    num_list = [int(input()) for i in range(int(input()))]
    
    num_list.sort()
    
    for i in num_list:
        print(i)

if __name__ == "__main__":
    ascending_sort()