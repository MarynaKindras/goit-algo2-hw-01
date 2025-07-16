from colorama import Fore, Style

def quick_select(arr, k):
    """
    Finds the k-th smallest element in an array using the Quick Select
    algorithm.

    Args:
        arr (list): Input array of numbers.
        k (int): Index (starting from 0) of the k-th smallest element.

    Returns:
        int: The k-th smallest element.
    """
    if len(arr) == 1:  # Якщо в масиві лише один елемент, повертаємо його
        return arr[0]

    pivot = arr[len(arr) // 2]  # Вибір опорного елемента (pivot)
    less = [x for x in arr if x < pivot]  # Масив елементів, менших за pivot
    equal = [x for x in arr if x == pivot]  # Масив елементів, рівних pivot
    greater = [x for x in arr if
               x > pivot]  # Масив елементів, більших за pivot

    if k < len(less):  # Якщо k-й елемент знаходиться у меншій підгрупі
        return quick_select(less, k)
    elif k < len(less) + len(equal):  # Якщо k-й елемент є pivot
        return equal[0]
    else:  # Якщо k-й елемент у більшій підгрупі
        return quick_select(greater, k - len(less) - len(equal))


if __name__ == "__main__":
    arr = [3, 5, 1, 8, -1, 10, 2]
    k = 3
    # k-1 because indexing starts from 0
    kth_smallest = quick_select(arr, k - 1)
    print(
        Fore.YELLOW + f"{k}-th smallest element: {kth_smallest}"
        + Style.RESET_ALL
    )