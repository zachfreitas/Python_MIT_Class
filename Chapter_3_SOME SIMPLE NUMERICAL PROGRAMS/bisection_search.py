
# -*- coding: utf-8 -*-

""""
Approximating the square root using bisection search

"""
# x = 25 # Answer is 5
# x = 123456 # Answer is 351.363060095964
x = -25
epsilon = 0.01
numGuesses = 0 
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2-x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)


# def main():
#     x = int(input('Enter an integer: '))
#     cube_root(x)

# if __name__ == "__main__":
#      main()

