# Branching Examples

def is_even(x):
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
