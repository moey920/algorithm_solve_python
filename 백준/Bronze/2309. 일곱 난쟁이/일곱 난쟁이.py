import sys

def find_seven_small_man():
    small_man = [int(sys.stdin.readline().strip()) for _ in range(9)]
    small_man.sort()

    total_sum = sum(small_man)
    
    for i in range(len(small_man)):
        for j in range(i+1, len(small_man)):
            if total_sum - (small_man[i] + small_man[j]) == 100:
                del small_man[i]
                del small_man[j-1]
                return small_man
                


if __name__ == "__main__":
    small_man = find_seven_small_man()
    for i in small_man:
        print(i)