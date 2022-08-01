import sys

def pokemon_master():
    """
    첫째 줄에 정수의 개수 n ,m이 주어진다.
    n개의 줄에는 첫 문자, 혹은 마지막 문자가 대문자이고 나머지는 소문자인,
    2이상, 20 이하의 문자열이 주어진다.
    m개의 줄에는 첫 문자, 혹은 마지막 문자가 대문자이고 나머지는 소문자인 문자열이나
    정수가 주어진다.
    
    Args:
        None
    
    Returns:
        m번째 줄의 값이 문자열이면 n개의 줄에서 해당되는 문자열의 인덱스 값을,
        정수이면 n개의 줄에서 해당되는 인덱스의 문자열 값을 리턴한다.
    """
    n, m = map(int, sys.stdin.readline().split())
    pokemon_dict = {}
    
    # # 시간초과로 제외
    # def get_key_from_value(d, val):
    #     """중복 값이 ​​없는 사전의 경우
    #     지정된 값을 가진 키가 있으면 해당 키가 반환되고, 그렇지 않으면 None을 반환됩니다. 값이 중복되면 키 중 하나가 반환됩니다.

    #     Args:
    #         d (dict): dictionay
    #         val (None): value

    #     Returns:
    #         str: Search dict's key by value
    #     """
    #     keys = [k for k, v in d.items() if v == val]
    #     if keys:
    #         return keys[0]
    #     return None
    
    for i in range(1, n+1):
        a = sys.stdin.readline().strip()
        pokemon_dict[i] = a
        pokemon_dict[a] = i
    
    input_list = [sys.stdin.readline().strip() for i in range(m)]
    
    
    for pokemon in input_list:
        if pokemon.isdigit():
            print(pokemon_dict[int(pokemon)])
        else:
            print(pokemon_dict[pokemon])
    
    
if __name__ == "__main__":
    pokemon_master()