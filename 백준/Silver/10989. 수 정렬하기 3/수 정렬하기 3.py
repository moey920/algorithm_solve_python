def ascending_counting_sort():
    """
    N 자리수의 숫자를 줄 별로 입력받아, 오름차순으로 정렬한 뒤 N줄로 반환합니다.
    
    수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.
    두 수를 반복적으로 비교해 정렬하는 comparison sort는 아무리 알고리즘을 잘 짜도 계산 복잡성이 O(nlogn)보다 큽니다.
    
    1. 각 숫자의 빈도를 저장하기 위한 배열 생성
    2. 각 숫자에 해당하는 인덱스에 빈도수 저장 (따라서 리스트의 모든 원소는 양의 정수여야 한다)
    3. 배열을 탐색하며 저장된 빈도수만큼 인덱스 출력
    다만 n의 값이 너무 커지면 불필요한 메모리 공간이 많이 낭비될 수 있어 비효율적이고, 일반 정렬 알고리즘보다 느려질 수도 있다.
    정렬을 위한 길이 n의 배열 하나, 계수를 위한 길이 k의 배열 하나. O(n+k) 의 공간복잡도를 가진다.
    
    주의점. 내장 정렬 함수는 시간 복잡도를 만족하지 못한다. list.append 함수는 O(1) 시간 복잡도를 가진다, list.count() 내장 함수는 O(n)의 시간 복잡도를 가진다.

    input:
        입력받을 정수의 수 N, N개만큼의 줄로 나뉜 정수
        
    return:
        N개의 정수를 오름차순으로 정렬하여 반환
    """
    import sys
    
    input = sys.stdin.readline
    
    # 10000 이하의 자연수를 카운팅 할 리스트 선언
    num_list = [0 for _ in range(10001)]
    N = int(input())
    
    # 정수값을 카운트한 배열을 생성한다.
    for _ in range(N):
        num = int(input())
        num_list[num] += 1
    
    # 배열의 시작부터 돌며 저장된 빈도만큼 인덱스값을 출력
    for i in range(1, 10001):
        count = num_list[i]
        for _ in range(count):
            print(i)

if __name__ == "__main__":
    ascending_counting_sort()