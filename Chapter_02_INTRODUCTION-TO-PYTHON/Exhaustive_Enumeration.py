# -*- coding: utf-8 -*-
# Exhaustive Enumeration
# This is a variant of guess and check

"""Works almost as fast with 7406961012236344616 and it does with 27. Impressive.
"""

def cube_root(x):
    """Find the cube root of a perfect cube

    Args:
        x (int): number you are trying to determine is a cube root

    Returns:
        None: Function just prints results.
        
    """
    ans = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans 
        print('Cube root of', x, 'is', ans)
    return None


def main():
    x = int(input('Enter an integer: '))
    cube_root(x)

if __name__ == "__main__":
     main()