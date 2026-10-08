# SAME AS SORT ARRAY, JUST CHANGE last_element <= stack[-1] to push smallest element at last


def check_and_insert_stack_element(stack: list[int], last_element: int) -> list[int]:
    if len(stack) == 0 or last_element <= stack[-1]:
        stack.append(last_element)
        return stack

    last_item = stack.pop()
    check_and_insert_stack_element(stack, last_element)
    stack.append(last_item)

    return stack


def reverse_stack(stack: list[int]) -> list[int]:
    # base case - stack of length 0 and 1 are already reversed by default :)
    if len(stack) == 0 or len(stack) == 1:
        return stack

    # hypothesis case n-1
    last_element = stack.pop()

    stack = reverse_stack(stack)

    return check_and_insert_stack_element(stack, last_element)


def main():
    n = int(input("Enter the length of stack: "))
    stack = []
    for i in range(n):
        stack.append(int(input("Enter stack element: ")))

    print(reverse_stack(stack))


if __name__ == "__main__":
    main()
