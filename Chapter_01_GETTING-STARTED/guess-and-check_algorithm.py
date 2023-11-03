""""
# Adequate Approximation to the square root of N.

Imperative knowledge is “how to” knowledge, or recipes for deducing information. 

Heron of Alexandria was the first to document a way to compute the square root of a number.2 
His method for finding the square root of a number, call it x, can be summarized as:

Start with a guess, g. 
If g*g is close enough to x, stop and say that g is the answer. 
Otherwise create a new guess by averaging g and x/g, i.e., (g + x/g)/2. 
Using this new guess, which we again call g, repeat the process until g*g is close enough to x. 

Consider, for example, finding the square root of 25. 

Set g to some arbitrary value, e.g., 3. 
We decide that 3*3 = 9 is not close enough to 25. 
Set g to (3 + 25/3)/2 = 5.67.3 
We decide that 5.67*5.67 = 32.15 is still not close enough to 25. 
Set g to (5.67 + 25/5.67)/2 = 5.04 
We decide that 5.04*5.04 = 25.4 is close enough, so we stop and declare 5.04 to be an adequate approximation to the square root of 25.

Many believe that Heron was not the inventor of this method, 
and indeed there is some evidence that it was well known to the ancient Babylonians.

"""
target = int(input("Enter Square Root: "))
tolerance = 0.4
diff = 100
guess = 3

def answer(target, guess, diff, tolerance):
    return print("Target:",target, "Guess:", guess, "Difference:", diff,"Tolerance:",tolerance)

if target == 0:
    guess = "The Square Root of Zero is Undefined."
    diff = 0
    answer(target, guess, diff, tolerance)
elif target == 1:
     guess = 1
     diff = 0
     answer(target, guess, diff, tolerance)
else:
    while diff >= tolerance:
        guess = (guess + target/guess)/2 
        diff = abs((guess * guess) - target)
    answer(target, guess, diff, tolerance)







