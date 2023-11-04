def isPalindrome(s):
    """Assumes s is a string aka str
    returns True if letters in s for a palindrom; False otherwise.
    Non-letters and capitalization are ignored."""
    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters 
    
    def isPal(s):
        """ Recursive Function to see if letters match 
            returns True or False"""
        if len(s) <= 1:
            """Base Case"""
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))


# Test Case
def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))
        
