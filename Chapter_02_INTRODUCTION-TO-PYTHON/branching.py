# -*- coding: utf-8 -*-
# Branching Examples

def is_even(x):
    """Determine if an integer is even or odd.

    Args:
        x (int): number you are trying to determin as odd or even.

    Returns:
        None: Function just prints results.
        
    """
    if x%2 == 0: 
        print('Even') 
    else: print('Odd') 
    print('Done with conditional')
    return None


def main():
    x = int(input("Enter Integer: "))
    is_even(x)

if __name__ == "__main__":
     main()
