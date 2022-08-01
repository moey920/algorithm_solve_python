import sys


def number_card():
    """
    N개의 카드 개수와 N개의 카드를 각각 입력받고
    N개의 카드 중
    M개의 카드 개수와 M개의 카드를 각각 입력받는다.
    N과 M의 각 카드가 겹치는 경우는 없다.
    
    params:
        None
    
    returns:
        N과 M이 겹치면 1, 아니면 0을 반환한다.    
    """
    input = sys.stdin.readline
    
    
    def check_assert(card_count: int, card_list: list):
        assert len(card_list) == card_count, "카드의 개수가 잘못되었습니다"
    
    
    n_card_count = int(input())
    n_card_list = set(map(int, input().split()))
    check_assert(n_card_count, n_card_list)
    
    m_card_count = int(input())
    m_card_list = list(map(int, input().split()))
    check_assert(m_card_count, m_card_list)
    
    for m_card in m_card_list:
        # x in list보다 x in set이 빠르다.
        if m_card in n_card_list:
            print("1", end=' ')
        else:
            print("0", end=' ')
            
            
if __name__ == "__main__":
    number_card()