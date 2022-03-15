import math
import sys

def lcm(a,b):
    return (a * b) // math.gcd(a,b)
        
if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(lcm(a,b), math.gcd(a,b))