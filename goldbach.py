def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number "))
if num % 2 == 0:
    for i in range(3,num,2):
        j = num-i
        if isPrime(i) and isPrime(j):
            print("Goldbach number ")
            break
else:
    print("Not a goldbach number ")
