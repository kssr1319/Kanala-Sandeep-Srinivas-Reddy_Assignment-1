# 1. Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

n1 = 0
n2 = 1
while n2 in range (0,50):
    n = n1 + n2
    n1 = n2
    n2 = n
    if n2<=50:
        print (n2)