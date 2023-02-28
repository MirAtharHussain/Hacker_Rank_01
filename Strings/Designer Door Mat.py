"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints
5<N<101
15<M<303

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
#below code by me


N, M = map(lambda x:int(x), input().split())
dash = '-'
pattern = '.|.'

for i in range(1,(N-2)+1,2):
    print((pattern*i).center(M,dash))

if (N//2+1):
    print('WELCOME'.center(M,dash))

for i in range(N-2,-1,-2):
    print((pattern*i).center(M,dash))


'''
N, M = map(lambda x:int(x), input().split())
dash = '-'
pattern = '.|.'


for i in range(1, N+1):
    
    if (i % 2 == 1):
        print(i)
        print((pattern*i).center(M,dash))
    
    if i == (N//2)+1:
        print('WELCOME'.center(M,dash))
'''