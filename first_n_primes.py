limit = int(input("Please enter a maximum limit: "))
num = 1

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# While loop to print prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
while num <= limit:
    if is_prime(num):
        print(num)
    num += 1