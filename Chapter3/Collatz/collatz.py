def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1
        
    print(value)
    return value


number = input("Please enter a number: ")

try:

    number = int(number)

    while number != 1:
        number = collatz(number)
        
except ValueError:
    
    print("This is not a number")