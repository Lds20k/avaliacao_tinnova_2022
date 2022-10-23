def bubble_sort(numbers):
    sorted_numbers = numbers.copy()
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if(sorted_numbers[j] > sorted_numbers[j + 1]):
                aux = sorted_numbers[j + 1]
                sorted_numbers[j + 1] = sorted_numbers[j]
                sorted_numbers[j] = aux
    return sorted_numbers

if __name__ == "__main__":
    my_numbers = [5, 3, 2, 4, 7, 1, 0, 6]
    print(my_numbers)
    print(bubble_sort(my_numbers))