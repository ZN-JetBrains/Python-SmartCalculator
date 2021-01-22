# Author: Zaid Neurothrone

from collections import deque


class Calculator:
    """Class description."""

    supported_operations = ["+", "-", "*", "/", "//", "%", "**"]

    def __init__(self):
        pass

    @staticmethod
    def process_expression(exp):
        while exp.count("--") >= 1 or exp.count("++") >= 1:
            exp = exp.replace("--", "+")
            exp = exp.replace("++", "+")
            exp = exp.replace("+-", "-")
        exp_list = exp.split(" ")

        processed_list = []

        for x in exp_list:
            if x:
                processed_list.append(x)

        return Calculator.compute_expression(processed_list)

    @staticmethod
    def compute_expression(processed_list):
        numbers = deque()
        operators = deque()

        for element in processed_list:
            if element in Calculator.supported_operations:
                operators.append(element)
            else:
                numbers.append(int(element))

        while len(numbers) > 1:
            operation = operators.popleft()
            operand_a = numbers.popleft()
            operand_b = numbers.popleft()

            result = 0
            if operation == "+":
                result = Calculator.add(operand_a, operand_b)
            elif operation == "-":
                result = Calculator.subtract(operand_a, operand_b)
            numbers.appendleft(result)
        return numbers.pop()

    @staticmethod
    def add(a, b):
        return a + b
    # def add(numbers):
    #     return sum(numbers)

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
            print("The program computes operations containing additions and subtractions.")
            continue

        print(Calculator.process_expression(user_input))

        # print(eval(user_input))

        # IF only one number is entered
        # if len(input_list) < 2:
        #     print(int(input_list[0]))
        #     continue

        # Sum all numbers
        # numbers = [int(x) for x in input_list]
        # print(Calculator.add(numbers))


if __name__ == "__main__":
    run()
