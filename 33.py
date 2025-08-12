#a
def is_palindrome(num):
    return str(num) == str(num)[::-1]

print(is_palindrome(int(input("Enter a number: "))))

# b
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(int(input("Enter a number: "))))
