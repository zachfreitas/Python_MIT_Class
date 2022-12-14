# -*- coding: utf-8 -*-
# Iteration or Looping Examples

# Square an integer, the hard way 
print('#'*100)
string = 'Square an integer, the hard way'
print(string)
print('#'*len(string))
x = 3 
ans = 0 
itersLeft = x 
while (itersLeft != 0): 
    ans = ans + abs(x) 
    itersLeft = itersLeft - 1 
    print(str(x) + '*' + str(x) + ' = ' + str(ans))


#Find a positive integer that is divisible by both 11 and 12 
print('#'*100)
string = 'Find a positive integer that is divisible by both 11 and 12'
print(string)
print('#'*len(string))
x = 1 
while True: 
    if x%11 == 0 and x%12 == 0: 
        break 
    x = x + 1 
print(x, 'is divisible by 11 and 12')
