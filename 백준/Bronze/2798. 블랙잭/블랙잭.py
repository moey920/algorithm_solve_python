def black_jack(n ,m):
    card_list = list(map(int, input().split()))
    result = 0
    for i in range(len(card_list)):
        for j in range(i+1, len(card_list)):
            for z in range(j+1, len(card_list)):
                if card_list[i]+card_list[j]+card_list[z] > m:
                    continue
                else:
                    result = max(result, card_list[i]+card_list[j]+card_list[z])
    
    print(result)

if __name__ == "__main__":
    n, m = map(int, input().split())
    black_jack(n ,m)