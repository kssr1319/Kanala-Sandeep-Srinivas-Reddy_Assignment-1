# 3. Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

numbers = [11,13,12,14,15,16,22,21,2,23,18,1,3,8,9]
a = 0
b = 0
for n in numbers:
    if n % 2 == 0:
        a +=1
    else:
        b +=1
print("Number of even numbers: ", a)
print("Number of odd numbers: ", b)