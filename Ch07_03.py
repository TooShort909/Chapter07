def rainfall_statistics():
    rainfall = []
    
    # Get rainfall data for each month
    for month in range(1, 13):
        rain = float(input(f"Enter the rainfall for month {month}: "))
        rainfall.append(rain)
    
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)
    
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    
    # Find the months with highest and lowest rainfall
    max_month = rainfall.index(max_rainfall) + 1
    min_month = rainfall.index(min_rainfall) + 1
    
    # Display the results
    print(f"Total rainfall for the year: {total_rainfall} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with highest rainfall: Month {max_month} ({max_rainfall} inches)")
    print(f"Month with lowest rainfall: Month {min_month} ({min_rainfall} inches)")
    
rainfall_statistics()