def total_sales():
    sales = []  # Create an empty list to store the sales amounts
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Get sales for each day
    for day in days_of_week:
        sale = float(input(f"Enter the sales for {day}: "))
        sales.append(sale)

    # Calculate total sales for the week
    total = sum(sales)
    
    # Display the result
    print(f"Total sales for the week: ${total:.2f}")
    
total_sales()