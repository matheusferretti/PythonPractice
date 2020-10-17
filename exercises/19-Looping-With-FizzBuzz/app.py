def fizz_buzz():
    # your code here
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"

fizz_buzz()