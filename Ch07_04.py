def number_analysis():
    numbers = []
    
    # Get 20 numbers from the user
    for i in range(1, 21):
        number = float(input(f"Enter number {i}: "))
        numbers.append(number)
    
    # Calculate the lowest, highest, total, and average
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    # Display the results
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")
    
number_analysis()