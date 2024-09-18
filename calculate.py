import random
import time

def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if the discount is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def slow_print(message, delay=0.05):
    """Print message with a typing effect."""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    compliments = [
        "Awesome choice!",
        "You're a savvy shopper!",
        "Great deal hunter!",
        "You have excellent taste!",
        "You deserve this discount!"
    ]

    slow_print("🎉 Welcome to the Ultimate Discount Calculator! 🎉")
    time.sleep(1)

    try:
        # Prompt the user for input with playful messages
        slow_print("🛒 Let's find out how much you can save today!")
        original_price = float(input("Enter the original price of the item (e.g., 100.00): $"))
        discount_percent = float(input("Enter the discount percentage (e.g., 25): "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Provide feedback with fun messages
        if discount_percent >= 20:
            compliment = random.choice(compliments)
            slow_print(f"🎉 Hooray! Your discount of {discount_percent}% means you save big!")
            slow_print(f"Your final price is: ${final_price:.2f}")
            slow_print(f"💬 {compliment}")
        else:
            slow_print(f"😅 Oh no! Your discount of {discount_percent}% is less than 20%.")
            slow_print(f"The original price stays at: ${final_price:.2f}")
            slow_print("But don't worry, there will be better deals ahead!")
        
    except ValueError:
        slow_print("🚫 Uh-oh! Please enter valid numerical values for the price and discount percentage. Try again!")

# Run the interactive function
main()
