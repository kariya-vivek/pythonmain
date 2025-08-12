def is_armstrong(num):
    power = len(str(num))
    return num == sum(int(digit)**power for digit in str(num))

print(is_armstrong(int(input("Enter a number: "))))
