def population_data():
    # Read the population data from the file
    with open('USPopulation.txt', 'r') as file:
        population_data = [int(line.strip()) for line in file.readlines()]

    # Calculate annual population changes
    changes = [population_data[i] - population_data[i - 1] for i in range(1, len(population_data))]
    
    # Find the average annual change
    average_change = sum(changes) / len(changes)

    # Find the year with the greatest increase and the smallest increase
    max_increase = max(changes)
    min_increase = min(changes)
    max_year = changes.index(max_increase) + 1951  # Add 1951 because the first data is for 1950
    min_year = changes.index(min_increase) + 1951

    # Display results
    print(f"Average annual population change: {average_change:.2f} thousand people")
    print(f"The year with the greatest population increase: {max_year} ({max_increase} thousand people)")
    print(f"The year with the smallest population increase: {min_year} ({min_increase} thousand people)")

population_data()