def insert(arr: list[int], last_element: int):
    if len(arr) == 0 or arr[-1] <= last_element:
        arr.append(last_element)
        return arr

    last = arr[-1]
    arr = arr[:-1]
    arr = insert(arr, last_element)
    arr.append(last)

    return arr


def sort_an_array(arr: list[int]):
    # base case to return when array is of length 1
    if len(arr) == 1:
        return arr

    # pop the last element to sort smaller subset - hypothesis step (n-1) hehe
    last_element = arr[-1]
    arr = arr[:-1]
    arr = sort_an_array(arr)

    return insert(arr, last_element)


def main():
    array = []
    n = int(input("Enter length of array: "))

    for item in range(0, n):
        array.append(int(input("Enter Element: ")))

    print(sort_an_array(array))


if __name__ == "__main__":
    main()
