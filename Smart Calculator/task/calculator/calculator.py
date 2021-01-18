# Author: Zaid Neurothrone

class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(numbers):
        return sum(numbers)

    @staticmethod
    def add_args(*args):
        sum_ = 0
        for num in args:
            sum_ += num
        return sum_

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def divide(a, b):
        if not b:
            return 0
        return a / b

    @staticmethod
    def divide_integer(a, b):
        if not b:
            return 0
        return a // b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def modulus(a, b):
        return a % b

    @staticmethod
    def power(a, b):
        return a ** b


def run():
    while True:
        user_input = input()

        # IF no input is entered
        if not user_input:
            continue

        if user_input == "/exit":
            print("Bye!")
            break

        if user_input == "/help":
            print("The program calculates the sum of numbers")
            continue

        input_list = user_input.split(" ")

        # IF only one number is entered
        if len(input_list) < 2:
            print(int(input_list[0]))
            continue

        # Sum all numbers
        numbers = [int(x) for x in input_list]
        print(Calculator.add(numbers))


if __name__ == "__main__":
    run()
