def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
print(f"The final price after discount (if applicable) is: {final_price:.2f}")
