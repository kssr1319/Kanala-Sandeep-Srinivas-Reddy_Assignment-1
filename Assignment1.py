# 2. Write a Python program that accepts a word from the user and reverse it.
# Sample Test Case

# Input : Edyoda
# output: adoydE

w =str(input("Enter your choice word:"))
r = str()
l = len(w)
while l > 0:
    r += w[l-1]
    l = l-1
print("Given word in reverse is:",r)