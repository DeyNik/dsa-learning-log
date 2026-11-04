The **two-pointer technique** is a fundamental algorithmic pattern used to solve problems involving arrays, strings, or linked lists. Instead of using nested loops that result in a slower $O(n^2)$ time complexity, this approach uses two reference points (pointers) that traverse the data structure, typically reducing the time complexity to $O(n)$ and auxiliary space to $O(1)$.

---

## 1. Core Patterns of Two Pointers

Depending on the problem structure, the two pointers move in specific ways to narrow down the search space.

### Pattern A: Opposite Ends (Left & Right Pointers)

- **How it works:** One pointer starts at the beginning (`left = 0`) and the other starts at the end (`right = n - 1`). They move toward each other until they meet or cross.
- **When to use:** Sorted arrays, searching for pairs with specific sums, palindrome checks, or optimizing container boundaries.
- **Classic Examples:**
- _Two Sum II - Input Array Is Sorted_
- _Valid Palindrome_
- _Container With Most Water_

### Pattern B: Same Direction (Fast & Slow Pointers)

- **How it works:** Both pointers start at the beginning, but they move at different speeds or intervals based on specific conditions.
- **When to use:** In-place array modifications, cycle detection in linked lists, or finding specific elements in a sequence.
- **Classic Examples:**
- _Remove Duplicates from Sorted Array_
- _Linked List Cycle Detection (Floyd's Tortoise and Hare)_
- _Move Zeroes_

---

## 2. Classic Code Example: Valid Palindrome

Here is a classic implementation of the **Opposite Ends** pattern in Python to check if a string is a palindrome (ignoring non-alphanumeric characters and case):

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters case-insensitively
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

```

---

## 3. Advantages & Limitations

| Feature                | Details                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| **Time Complexity**    | Usually **$O(n)$**, as each element is visited at most once or a constant number of times.           |
| **Space Complexity**   | **$O(1)$** auxiliary space because pointers only require a few variables for indices.                |
| **Primary Limitation** | Often requires the underlying data structure to be **sorted** (for opposite-end problems) or linear. |

---

Would you like to walk through a specific problem or practice coding a two-pointer solution together?
