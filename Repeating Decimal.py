#!/usr/bin/env python
# coding: utf-8

# In[6]:

from time import sleep # For step-by-step display
d = int(input("Input a denominator: "))
print(f"1/{d} is computed")
count = 0 # Counter of the number of steps/decimals
done = False # Boolean used to detect end of computation
x = 1
remainders=""
i=1
number="0."
while not done: # Keep doing until termination is detected
    count += 1
    x = x * 10
    quotient = x // d
    remainder = x % d
    if str(remainder) in remainders.split("\'"): #Detect if the remainder has existed.
        done=True
        while str(remainder)!=remainders.split("\'")[i]: #Find which index in list.
            i+=1
    else:                                    
        remainders=remainders+"\'"+str(remainder)  #If the remainder hasn't exist, add it to will-turn-to-list string
    number=number+str(quotient) #add each decimal to the number
    if remainder == 0:
        done = True
    else:
        x = remainder
print(number[:]+"("+number[2+i:]+")") #print the repeating decimal in brackets from the decimal after index of repeating.

