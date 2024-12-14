from datetime import datetime, timedelta
import random
import math
from models.product import Product

def generate_test_data():
    products = []
    base_products = [
        {
            "product_id": "PROD001",
            "product_name": "Trending Gadget",
            "base_price": 29.99,
            "growth_pattern": "rising"
        },
        {
            "product_id": "PROD002",
            "product_name": "Seasonal Item",
            "base_price": 19.99,
            "growth_pattern": "seasonal"
        }
    ]

    # Get current timestamp for consistent dates
    now = datetime.now()
    
    # Generate 30 days of historical data
    for day in range(30):
        current_date = now - timedelta(days=30-day)
        
        for base_product in base_products:
            # Calculate order count based on pattern
            if base_product["growth_pattern"] == "rising":
                order_count = int(50 + (day * 2) + random.randint(-5, 5))
            elif base_product["growth_pattern"] == "seasonal":
                order_count = int(40 + (math.sin(day/7 * math.pi) * 20) + random.randint(-5, 5))
            
            # Ensure order_count is never negative
            order_count = max(0, order_count)
            
            # Calculate price with variation
            price = base_product["base_price"] * (1 + random.uniform(-0.1, 0.1))
            
            # Calculate review count and ensure it's not negative
            review_count = max(0, int(order_count * 0.3))
            
            # Create product instance
            product = Product(
                product_id=base_product["product_id"],
                product_name=base_product["product_name"],
                order_count=order_count,
                price=round(price, 2),
                review_count=review_count,
                rating=round(random.uniform(3.5, 5.0), 1),
                timestamp=current_date,
                daily_order_velocity=order_count,
                price_to_order_ratio=round(price/order_count if order_count > 0 else 0, 2)
            )
            products.append(product)

    return products 