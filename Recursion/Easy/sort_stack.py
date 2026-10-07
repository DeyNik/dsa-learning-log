def insert_stack(stack, last_element):
    # base case -> if stack is of length zero = there is nothing to insert
    # or if last element is greater than the stack's last item, simply insert and return
    if len(stack) == 0 or last_element >= stack[-1]:
        print(
            "insert_stack -> len of stack is 0 or element is greater than one: ", stack
        )
        stack.append(last_element)
        print("insert_stack -> added last element ", stack)

        return stack

    print("insert_stack -> getting last element ", stack)
    last_item = stack.pop()
    print("insert_stack -> removed last element ", stack)

    stack = insert_stack(stack, last_element)

    stack.append(last_item)
    print("insert_stack -> inserting back  last element ", stack)

    return stack


def sort_stack(stack: list[int]):
    # base case
    if len(stack) == 1:
        print("sort_stack -> len of stack is 1: ", stack)
        return stack

    # hypothesis: sort n-1 stack
    # get n-1 stack by removing last element
    last_element = stack.pop()
    print("sort_stack -> removed last element: ", stack, "last element:", last_element)
    stack = sort_stack(stack)
    print("sort_stack -> called sort stack: ", stack)

    # insert the last element to the sorted stack again
    return insert_stack(stack, last_element)


def main():
    n = int(input("Enter size of stack: "))
    stack = []
    for item in range(n):
        stack.append(int(input("Enter stack element: ")))

    # sort stack
    print(sort_stack(stack))


if __name__ == "__main__":
    main()
