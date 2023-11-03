
# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
# The following approach is called successive approximation.


epsilon = 0.01
# k = 24.0
k = 123456 # This take 11 guesses where bisection takes 30 
# k = -25
guess = k/2.0
count = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess)) # Guess minus the guess divided by first derivative of guess
    count += 1
print('Square root of', k, 'is about', guess, "Count:", count)



