import random

def lottery_number_generator():
    lottery_numbers = []
    
    # Generate a list of 7 random digits between 0 and 9
    for _ in range(7):
        lottery_numbers.append(random.randint(0, 9))
    
    # Display the lottery numbers
    print("Lottery Numbers: ", lottery_numbers)
    
lottery_number_generator()