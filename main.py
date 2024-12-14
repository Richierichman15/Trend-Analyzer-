from database.db import SessionLocal
from services.metrics import ProductMetrics
from services.trend_detector import TrendDetector
from services.data_generator import generate_test_data
from datetime import datetime
from models.product import Product

def setup_test_database():
    session = SessionLocal()
    
    # Clear existing data (optional, but helps ensure consistent state)
    session.query(Product).delete()
    
    # Generate fresh test data with current timestamps
    test_products = generate_test_data()
    
    for product in test_products:
        product.timestamp = datetime.now()  # Ensure current timestamp
        session.add(product)
    
    session.commit()
    return session

def main():
    session = setup_test_database()
    
    metrics = ProductMetrics(session)
    detector = TrendDetector(session)
    
    emerging_trends = detector.detect_emerging_trends()
    
    if not emerging_trends:
        print("No emerging trends found.")
        return
    
    # Print results
    for trend in emerging_trends[:5]:
        product = trend['product']
        confidence = trend['confidence']
        indicators = trend['indicators']
        
        print(f"\nProduct: {product.product_name}")
        print(f"Product ID: {product.product_id}")
        print(f"Confidence Score: {confidence:.2f}")
        print("Trend Indicators:")
        for indicator, value in indicators.items():
            print(f"  - {indicator}: {value:.2f}")
        print(f"Current Order Count: {product.order_count}")
        print(f"Current Price: ${product.price:.2f}")
        print(f"Review Count: {product.review_count}")
        print(f"Rating: {product.rating:.1f}")

if __name__ == "__main__":
    main()
