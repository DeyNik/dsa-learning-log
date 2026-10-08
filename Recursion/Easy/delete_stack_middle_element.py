def delete_middle_element(stack: list[int], middle_element_index) -> list[int]:
    """
    delete middle element of stack using recursion. This question is easy, just use the base case, hypothesis template and voila!

    Args:
    stack = original stack
    middle_element_index = the index element to delete. We use upper middle in case of even length stack

    Return:
    list of integer , which is the updated stack
    """
    # base case
    print("middle element index: ", middle_element_index)

    if len(stack) == 0:
        return []

    if middle_element_index == 0:
        stack.pop()
        return stack

    # hypothesis proof for n-1
    print("stack: ", stack)
    last_element = stack.pop()
    print("Pop last element: ", last_element)
    stack = delete_middle_element(stack, middle_element_index - 1)

    stack.append(last_element)
    print("push last element after deleting: ", stack)

    return stack


def main():
    n = int(input("Enter length of stack: "))
    stack = []
    for i in range(n):
        stack.append(int(input("Enter Stack element: ")))

    # Indexing from zero
    # for even elements we delete the upper middle , for lower middle do (n-1)//2
    print("middle element index: ", n // 2, " middle element: ", stack[(n - 1) // 2])
    print(delete_middle_element(stack, n // 2))


if __name__ == "__main__":
    main()
