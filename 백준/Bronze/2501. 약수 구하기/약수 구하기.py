def divisor_k():
    """
    args:
    
    input:
        n: 약수를 구할 대상인 수
        k: 약수 중 k번째 작은 수
        
    return:
        약수의 개수가 k보다 작으면 0, k보다 크면 k번째 약수를 반환
    """
    n, k = map(int, input().split())
    divisor = []
    
    for i in range(1, n+1):
        if n%i == 0:
            divisor.append(i)
    
    if len(divisor) < k :
        print("0")
    else:
        divisor.sort()
        print(divisor[k-1])
                
                
if __name__ == "__main__":
    divisor_k()