from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)


# Add Sample Inputs
price, quantity = 450.00, 3

total = calculate_total(price, quantity)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)  # Applying a 10% discount

print(f"Total: ${total:.2f}")
print(f"Requires Review: {review}")
print(f"Approval Tier: {tier}")
print(f"10% discount: ${discounted_price:.2f}")
