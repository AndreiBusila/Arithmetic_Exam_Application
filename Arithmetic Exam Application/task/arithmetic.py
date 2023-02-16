import random

operators = ["+", "-", "*"]


def mini_calculator(x, opt, y):
    if opt == "+":
        return x + y
    elif opt == "-":
        return x - y
    elif opt == "*":
        return x * y


def check_input_level():
    while True:
        try:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            user_input = int(input())
            if 1 <= user_input <= 2:
                return user_input
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def check_input():
    while True:
        try:
            user_input = int(input())
            return user_input
        except ValueError:
            print("Incorrect format.")


def level_one():
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    count = 0
    for i in range(5):
        operator = random.choice(operators)
        result = mini_calculator(x, operator, y)
        print(f"{x} {operator} {y}")
        user_input = check_input()
        if user_input == result:
            print("Right!")
            count += 1
        else:
            print("Wrong!")
    return count


def level_two():
    x = random.randint(11, 29)
    count = 0
    for i in range(5):
        result = pow(x, 2)
        print(f"{x}")
        user_input = check_input()
        if user_input == result:
            print("Right!")
            count += 1
        else:
            print("Wrong!")
    return count


opts = ["yes", "YES", "Yes", "y"]


def main():

    input_level = check_input_level()

    if input_level == 1:
        mark = level_one()
        print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
        user_input = input()
        if user_input in opts:
            user_name = input("What is your name?\n")
            file = open("results.txt", "a", encoding='utf-8')
            file.write(f"{user_name}: {mark}/5 in level 1 (simple operations with numbers 2-9).\n")
            file.close()
            print("The results are saved in \"results.txt\".")

    elif input_level == 2:
        mark = level_two()
        print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
        user_input = input()
        if user_input in opts:
            user_name = input("What is your name?\n")
            file = open("results.txt", "a", encoding='utf-8')
            file.write(f"{user_name}: {mark}/5 in level 2 (integral squares of 11-29).\n")
            file.close()
            print("The results are saved in \"results.txt\".")




main()
