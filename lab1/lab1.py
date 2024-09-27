#-----------------------------------------------------------------------
# FairCoin2.py
#
# Simulates n flips of a fair coin.
#
#-----------------------------------------------------------------------
from random import random

trials = 1000;
n = 100         # number of flips to perform
bobWin = 0;
p=0.5;

for j in range(trials):
    # perform n+1 flips
    bobHeads = 0;
    for i in range(n+1):

       # perform one flip
       x = random() # get a random number in [0.0, 1.0)
       
       if x < p:
           bobHeads+=1

    aliceHeads = 0;
    # perform n flips
    for i in range(n):

       # perform one flip
       x = random() # get a random number in [0.0, 1.0)
       
       if x < p:
           aliceHeads+=1
    
    #print("Bob:", bobHeads)
    #print("Alice:", aliceHeads)
    if bobHeads > aliceHeads:
        bobWin+=1
        #print(bobWin);
rFrequency = bobWin/trials;
print("n:", n)
print("Number of trials:", trials)
print()
print("Non-loaded coins: ")
print("p:", p)
print("Bob tossed more heads than Alice", bobWin, "times.")
print("Relative frequency:", rFrequency);

#loaded coin tests
print()
print("Loaded coin tests (Bob Advantage): ")
print("Bob trials:", n+1)
print("Alice trials:", n)
print("--------------------------")
print("p\trelative frequency")
print("--------------------------")
p=0.2
for k in range(1, 8):
    bobWin = 0;
    for j in range(trials):
        # perform n+1 flips
        bobHeads = 0;
        for i in range(n+1):

           # perform one flip
           x = random() # get a random number in [0.0, 1.0)
           
           if x < p:
               bobHeads+=1

        aliceHeads = 0;
        # perform n flips
        for i in range(n):

           # perform one flip
           x = random() # get a random number in [0.0, 1.0)
           
           if x < p:
               aliceHeads+=1
    
        #print("Bob:", bobHeads)
        #print("Alice:", aliceHeads)
        if bobHeads > aliceHeads:
            bobWin+=1
    rFrequency = bobWin/trials;
    print(p,"\t", rFrequency) 
    p += 0.1
    p=round(p, 1)


#loaded coin tests with alice advantage
print()
print("Loaded coin tests (Alice advantage):")
print("Bob trials:", n//2)
print("Alice trials:", n)
print("--------------------------")
print("p\trelative frequency")
print("--------------------------")
p=0.2
for k in range(1, 8):
    aliceWin = 0
    for j in range(trials):
        # perform n+1 flips
        bobHeads = 0;
        for i in range(n//2):

           # perform one flip
           x = random() # get a random number in [0.0, 1.0)
           
           if x < p:
               bobHeads+=1

        aliceHeads = 0;
        # perform n flips
        for i in range(n):

           # perform one flip
           x = random() # get a random number in [0.0, 1.0)
           
           if x < p:
               aliceHeads+=1
    
        #print("Bob:", bobHeads)
        #print("Alice:", aliceHeads)
        if bobHeads < aliceHeads:
            aliceWin+=1
    
    #print("Alice's Wins:", aliceWin)
    rFrequency = aliceWin/trials;
    print(p,"\t", rFrequency) 
    p += 0.1
    p=round(p, 1)

