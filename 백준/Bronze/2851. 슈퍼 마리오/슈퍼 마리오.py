import sys

def get_max_score():
    """
    args:
        None
    
    input:
        10개의 줄에 100이하의 양의 정수를 입력받는다.
        
    return:
        첫 입력 값부터 순서대로 입력 값을 더해 100에 가까운 값을 출력한다.
    """
    mushrooms = [int(sys.stdin.readline().strip()) for _ in range(10)]
    score = 0
    
    for mushroom in mushrooms:
        score += mushroom
        if score >= 100:
            if abs(score-100) <= abs(100-(score-mushroom)):
                return score
            else:
                return score-mushroom
    
    # sum of score > 100 
    return score
            
    
if __name__ == "__main__":
    score = get_max_score()
    print(score)