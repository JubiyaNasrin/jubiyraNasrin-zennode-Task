prices = {"Product A": 20, "Product B": 40, "Product C": 50}

def calculate_discounts(subtotal, quantity, totalquantity):
    discounts = {'flat_10_discount': 0, 'bulk_10_discount': 0, 'tiered_50_discount': 0}
    
    if subtotal > 200:
        discounts['flat_10_discount'] = 10
    
    if totalquantity > 10:
        discounts['bulk_10_discount'] = subtotal * 0.05
    if totalquantity > 20:
        discounts['bulk_10_discount'] = subtotal * 0.10

    if totalquantity > 30:
        for product, qty in quantity.items():
            if qty > 15:
                excess_quantity = qty - 15
                discounts['tiered_50_discount'] += excess_quantity * prices[product] * 0.5

    best_discount = max(discounts, key=discounts.get)
    return best_discount, discounts[best_discount]

def calculate_shipping(total_quantity):
    number_of_packages = (total_quantity + 9) // 10
    return number_of_packages * 5

def cart():
    quantities = {}
    gift_wraps = {}
    subtotal = 0

    for product in prices:
        qty = int(input(f"Enter quantity for {product}: "))
        wrap = input(f"Is {product} a gift? (yes/no): ")
        quantities[product] = qty
        gift_wraps[product] = wrap
        subtotal += qty * prices[product]

    total_quantity = sum(quantities.values())
    shipping_fee = calculate_shipping(total_quantity)
    gift_wrap_fee = sum(1 for wrap in gift_wraps.values() if wrap) * 5
    discount_name, discount_amount = calculate_discounts(subtotal, quantities, total_quantity)
    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee

    for product, qty in quantities.items():
        print(f"{product}: Quantity = {qty}, Total = ${qty * prices[product]}")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount Applied: {discount_name} (-${discount_amount})")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Total: ${total}")

if __name__ == "__main__":
    cart()
