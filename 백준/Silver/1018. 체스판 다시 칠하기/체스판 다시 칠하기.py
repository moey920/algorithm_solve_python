def fill_chaseboard():
    """
    정답 체스판과 인풋 체스판을 만들어 2차원 리스트의 인덱스를 하나씩 비교하여 다른 값을 찾아냅니다.
    input:
        n, m: 체스판의 가로, 세로 크기입니다.
        
    return:
        n*m크기의 체스판에서 변경 개수가 가장 적은 8*8 체스판을 잘라낸 뒤 두 체스판을 비교해서 다른 개수를 반환합니다.
    """
    n, m = map(int, input().split())
    input_board = [list(map(lambda x: 1 if x == "W" else 0, input())) for _ in range(n)]
    answer_board_1 = [[0 if (i+j)%2 else 1 for j in range(m)] for i in range(n)]
    answer_board_0 = [[1 if (i+j)%2 else 0 for j in range(m)] for i in range(n)]
    
    cnt_min = n*m
    for i in range(n-7):
        for j in range(m-7):
            cnt_1 = 0
            cnt_0 = 0
            for k in range(8):
                for l in range(8):
                    if answer_board_1[i+k][j+l] != input_board[i+k][j+l]:
                        cnt_1 += 1
                    if answer_board_0[i+k][j+l] != input_board[i+k][j+l]:
                        cnt_0 += 1
            # 최대 변경 개수인 cnt_min과 시작점에 따른 변경 개수은 cnt_1, cnt_0을 비교하여 최저값을 찾아낸다.
            if cnt_min > cnt_1:
                cnt_min = cnt_1
            if cnt_min > cnt_0:
                cnt_min = cnt_0
                
    print(cnt_min)

if __name__ == "__main__":
    fill_chaseboard()