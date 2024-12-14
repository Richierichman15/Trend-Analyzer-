from datetime import datetime, timedelta
from models.product import Product

class ProductMetrics:
    def __init__(self, session):
        self.session = session

    def calculate_metrics(self, product):
        return {
            'order_velocity': self._calculate_order_velocity(product),
            'growth_rate': self._calculate_growth_rate(product),
            'price_trend': self._calculate_price_trend(product),
            'market_saturation': self._calculate_market_saturation(product),
            'price_competitiveness': self._calculate_price_competitiveness(product)
        }

    def _calculate_order_velocity(self, product):
        seven_days_ago = datetime.now() - timedelta(days=7)
        recent_orders = self.session.query(Product)\
            .filter(Product.timestamp >= seven_days_ago)\
            .filter(Product.product_id == product.product_id)\
            .all()
        return len(recent_orders) / 7 if recent_orders else 0

    def _calculate_growth_rate(self, product):
        two_weeks_ago = datetime.now() - timedelta(days=14)
        historical_data = self.session.query(Product)\
            .filter(Product.timestamp >= two_weeks_ago)\
            .filter(Product.product_id == product.product_id)\
            .order_by(Product.timestamp)\
            .all()
        
        if len(historical_data) < 14:
            return 0
            
        week1_orders = sum(p.order_count for p in historical_data[:7])
        week2_orders = sum(p.order_count for p in historical_data[7:])
        
        return (week2_orders - week1_orders) / week1_orders if week1_orders > 0 else 0

    def _calculate_price_trend(self, product):
        return 0  # Implement price trend analysis

    def _calculate_market_saturation(self, product):
        return 0  # Implement market saturation analysis

    def _calculate_price_competitiveness(self, product):
        return 0  # Implement price competitiveness analysis