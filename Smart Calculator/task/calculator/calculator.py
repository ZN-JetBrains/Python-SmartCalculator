# Author: Zaid Neurothrone

class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

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

        if not user_input:
            continue

        if user_input == "/exit":
            print("Bye!")
            break

        input_list = user_input.split(" ")
        if len(input_list) < 2:
            print(int(input_list[0]))
            continue

        a, b = [int(x) for x in input_list]
        print(Calculator.add(a, b))


if __name__ == "__main__":
    run()
