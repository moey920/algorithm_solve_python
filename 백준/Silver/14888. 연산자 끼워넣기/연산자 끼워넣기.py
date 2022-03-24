import sys


n = int(input())
nums_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
maxi = -1000000001
mini = 1000000001

def dfs(i, result, sum, sub, mul, division):
    """
    셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
    """
    global maxi, mini
    
    if i == n:
        maxi = max(result, maxi)
        mini = min(result, mini)
        return
    
    else:
        if sum:
            dfs(i+1, result + nums_list[i], sum-1, sub, mul, division)
        if sub:
            dfs(i+1, result - nums_list[i], sum, sub-1, mul, division)
        if mul:
            dfs(i+1, result * nums_list[i], sum, sub, mul-1, division)
        if division:
            dfs(i+1, int(result / nums_list[i]), sum, sub, mul, division-1)
    


if __name__ == "__main__":
    input = sys.stdin.readline
    
    dfs(1, nums_list[0], operator_list[0], operator_list[1], operator_list[2], operator_list[3])
    print(maxi)
    print(mini)