from colorama import Fore, Style

def find_min_max(arr, low, high):
    """
    Finds the minimum and maximum elements in an array using the
    "divide and conquer" method.

    Args:
        arr (list): Input array of numbers.
        low (int): Starting index.
        high (int): Ending index.

    Returns:
        tuple: A tuple containing (minimum, maximum) values.
    """
    # Базовий випадок: якщо масив містить лише один елемент
    if low == high:
        return (arr[low], arr[high])

    # Якщо масив містить два елементи
    if high == low + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))

    # Рекурсивний випадок: розділяємо масив на дві частини
    mid = (low + high) // 2
    left_min, left_max = find_min_max(arr, low, mid)
    right_min, right_max = find_min_max(arr, mid + 1, high)

    # Знаходимо мінімум і максимум серед результатів обох частин
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return (overall_min, overall_max)

# Приклад використання
if __name__ == "__main__":

    arr = [3, 5, 1, 8, -1, 10, 2]
    min_val, max_val = find_min_max(arr, 0, len(arr) - 1)

    print(Fore.GREEN + f"Мінімальний елемент: {min_val}" + Style.RESET_ALL)
    print(Fore.RED + f"Максимальний елемент: {max_val}" + Style.RESET_ALL)