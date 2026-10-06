def factorial(n: int) -> int:
    """
    To print factorial of the given number

    Args:
    n = integer whose factorial is calculated

    Return:
    Integer which is the calculated factorial
    """
    # base case
    if n == 1 or n == 0:
        return n

    # induction + hypothesis
    # flow:
    # n=3
    # 3* command goes to factorial(2)
    # 2* command goes to factorial(1)
    # return 1 to caller n=2 as base case is met
    # return 2*1 to caller n=3
    # return 3*2*1 to main caller
    return n * factorial(n - 1)


def main():
    n = int(input("Enter number to calucate its factorial: "))
    fact = factorial(n)
    print(fact)


if __name__ == "__main__":
    main()
