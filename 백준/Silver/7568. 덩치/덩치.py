def human_rank():
    """
    args:
    
    input:
        N: 등급을 나눌 사람의 수
        x, y = 한 사람의 키와 몸무게
        
    return:
        x, y가 모두 다른 사람보다 큰 경우 랭크가 높다. 랭크는 같을 수도 있다. 랭크를 매겨 반환한다.
    """
    N = int(input())
    humans = []
    
    for _ in range(N):
        x, y = map(int, input().split())
        humans.append((x, y))

    for i in humans:
        rank = 1
        for j in humans:
            if i[0] < j[0] and i[1] < j[1]:
                rank +=1
        print(rank, end=" ")
                
                
if __name__ == "__main__":
    human_rank()