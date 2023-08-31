import sys
sys.stdin = open('input.txt')

def factorial(num1, result):
    if num1 == 1:
        print(result)
        return
    else:
        result = num1 * (num1 - 1)
        num1 -= num1
        factorial(num1)

N = int(input())

factorial(N, 0)



