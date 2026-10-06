def print_1_to_n(n: int):
    """
    Prints numbers from 1 to n

    Args:
    n -> an integer that defines the length of the sequence

    Return:
    None
    """

    # Base Case - What would stop the recursion?
    if n == 0:
        return

    # recursive call to get the next number
    print_1_to_n(n - 1)

    # print just after the last caller gets the command back from stop condition. How?
    # lets say the stack becomes:
    # print_1_to_n(3) -> print_1_to_n(2) ->print_1_to_n(1)-> print_1_to_n(0)
    # The flow becomes:
    # ( AI simplified flow)
    # 3 calls 2
    # 2 calls 1
    # 1 calls 0
    # 0 returns
    #     ↓
    # 1 executes pending print(1)
    #     ↓
    # 1 returns
    #     ↓
    # 2 executes pending print(2)
    #     ↓
    # 2 returns
    #     ↓
    # 3 executes pending print(3)

    print(n)


def print_n_to_1(n: int):
    """
    Prints numbers from n to 1

    Args:
    n -> an integer that defines the length of the sequence

    Return:
    None
    """
    # base case or stop condition
    if n == 0:
        return

    # print first then call for the next number to magically appear as descending.
    # Dont put the caller on wait for print

    print(n)
    print_n_to_1(n - 1)


def main():
    n = int(input("enter n: "))
    print_1_to_n(n)
    print_n_to_1(n)


if __name__ == "__main__":
    main()
