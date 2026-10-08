def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(input("Enter a number to caluculate its fibonacci: "))

    print(fibonacci(n))


if __name__ == "__main__":
    main()
