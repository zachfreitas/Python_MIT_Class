
# -*- coding: utf-8 -*-

""""
Approximating the square root using exhaustive enumeration

"""
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0 
ans = 0.0
while abs(ans**2-x) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)


# def main():
#     x = int(input('Enter an integer: '))
#     cube_root(x)

# if __name__ == "__main__":
#      main()



