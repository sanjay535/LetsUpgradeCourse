'''
Code to check primality of number
'''
N = int(input("Enter number to check prime or not"))
i = 2
while i*i <= N:
    if N%i == 0:
        print("Number is prime")
        break
print("Number is not prime")
