def binary_search(arr, x):
    counter = 0
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    if upper_bound < x:
        return -1
    while low <= high:
        counter += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (counter, arr[mid])

    # якщо елемент не знайдений
    return (counter, upper_bound)


arr = [2, 3, 4, 10, 40]
x = 4
result = binary_search(arr, x)
print(result)
