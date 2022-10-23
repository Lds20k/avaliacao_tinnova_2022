def factorial(number):
    return 1 if number in [0, 1] else number * factorial(number - 1)

if __name__ == "__main__":
    for i in range(0, 7):
        print(factorial(i))