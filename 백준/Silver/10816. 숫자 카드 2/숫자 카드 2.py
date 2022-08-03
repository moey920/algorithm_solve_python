import sys

def make_list_to_dict_by_count(object):
    """
    iterable한 객체의 요소와 카운트를 dictionary로 반환합니다.

    Args:
        object (object): iterable 객체

    Returns:
        counts (dict): 값의 개수에 따른 딕셔너리 반환
    """
    counts = {}
    for x in object:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts


def number_card():
    """
    정수 N과 N개만큼의 정수를 각각 입력받고
    정수 M과 M개만큼의의 정수를 각각 입력받는다.
    각 M개의 정수와 동일한 N개의 정수를 구하시오.
    
    params:
        None
    
    returns:
        N이 M안에 있는 숫자만큼을 공백으로 구분해 출력한다.
    """
    input = sys.stdin.readline    
    n_card_count = int(input())
    n_card_list = list(map(int, input().split()))
    m_card_count = int(input())
    m_card_list = list(map(int, input().split()))
    
    n_card_dict = make_list_to_dict_by_count(n_card_list)
    for m_card in m_card_list:
        try:
            print(n_card_dict[m_card], end=' ')
        except:
            print("0", end=' ')
            
            
if __name__ == "__main__":
    number_card()