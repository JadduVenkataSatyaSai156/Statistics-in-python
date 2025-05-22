#!/usr/bin/env python
# coding: utf-8

# In[1]:


# relative frequency for random tosses of a coin
import random
import itertools

results = {
    'heads': 0,
    'tails': 0,
}
sides = list(results.keys())

for i in range(1000):
    results[random.choice(sides)] += 1

print('Heads:', results['heads'])
print('Tails:', results['tails'])
# Calculating relative frequency for head and tail
rfh = results['heads']/1000 # Relative frequency for head of a coin
rft = results['tails']/1000 # Relative Frequecny for tail of a coin
print('Relative Frequency for head of a coin',rfh)
print('Relative Frequency for tail of a coin',rft)
# References
# 1).https://www.reddit.com/r/learnpython/comments/1ci995u/i_made_a_coin_flip_in_python_is_it_good_how_can_i/
# 2). https://dev.to/kelechikizito/python-tutorial-for-creating-a-coin-flip-simulation-56aa
# 3). https://github.com/Gataz/CoinToss/blob/main/cointoss.py
# 4). https://www.w3resource.com/python-exercises/math/python-math-exercise-53.php


# In[ ]:


# random dice experiment for two dices with the addition of the two dices at a toss
import random
x = "X"
y = "Y"
while x=="X" and y=="Y":
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    if n1==1 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==1 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==1 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==1 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==1 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==1 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==2 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==3 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==4 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==5 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==1:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==2:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==3:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==4:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==5:
        print(n1," ",n2," ","sum:",n1+n2)
    elif n1==6 and n2==6:
        print(n1," ",n2," ","sum:",n1+n2)
    x=input("press X to roll and e to exit")
    print("\n")
    y=input("press Y to roll and e to exit")
    print("\n")
# References
# 1). https://www.geeksforgeeks.org/dice-rolling-simulator-using-python-random/

