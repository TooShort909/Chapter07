def larger_than_n(numbers, n):
    # Display numbers greater than n
    print(f"Numbers greater than {n}:")
    for number in numbers:
        if number > n:
            print(number)

# Example usage
numbers_list = [1, 5, 8, 3, 7, 10, 15]
n = int(input("Enter a number to compare: "))
larger_than_n(numbers_list, n)