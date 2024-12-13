def charge_account_validation():
    # Read charge account numbers from the file
    with open('charge_accounts.txt', 'r') as file:
        accounts = [line.strip() for line in file.readlines()]
    
    # Ask the user to enter a charge account number
    account_number = input("Enter a charge account number: ")
    
    # Check if the number is valid
    if account_number in accounts:
        print("The charge account number is valid.")
    else:
        print("The charge account number is invalid.")
    
charge_account_validation()