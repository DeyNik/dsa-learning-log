def insert(arr: list[int], last_element: int):
    # base case: if element has length 0 or last_element is smaller than arr last element,
    # we can simply insert last element and return the array as it will be sorted
    if len(arr) == 0 or arr[-1] <= last_element:
        arr.append(last_element)
        return arr

    # else, pull out the last item from the array as that is greater than last_element passed
    # then again check if we can insert it one place earlier by trying with the smaller array length
    # hypothesis step :)
    last = arr[-1]
    arr = arr[:-1]
    # try inserting the last element in the array
    arr = insert(arr, last_element)
    # append teh array
    arr.append(last)

    return arr


def sort_an_array(arr: list[int]) -> list[int]:
    """
    For sorting the array. Why do we try sorting (n-1)? This is because it is important to break the array into
    smaller size and analyze each of its elements to sort it recusrively.
    In recursion, our decisions to always make the input smaller such that the problem can be minimized.
    Hence, this behaves as an template in most of the scenarios.

    Args: array
    Return: sorted array
    """
    # base case to return the list when array is of length 1 as it is already sorted
    if len(arr) == 1:
        return arr

    # pop the last element to sort smaller subset - hypothesis step (n-1)
    last_element = arr[-1]
    # trim the array
    arr = arr[:-1]
    # recursively call the array until it gets sorted
    arr = sort_an_array(arr)

    # insert the last element
    return insert(arr, last_element)


def main():
    array = []
    n = int(input("Enter length of array: "))

    for item in range(n):
        array.append(int(input("Enter Element: ")))

    print(sort_an_array(array))


if __name__ == "__main__":
    main()
