def decompose():
    """
    args:
    
    input:
        n: 자연수 N
        
    return:
        N의 가장 작은 생성자
    """
    n = int(input())
    
    for i in range(1, n+1):
        arr = list(map(int, str(i)))
        _sum = i + sum(arr)
        if _sum == n:
            print(i)
            break
        if i == n:
            print("0")
            break
        
                
if __name__ == "__main__":
    decompose()