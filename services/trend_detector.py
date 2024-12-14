from datetime import datetime, timedelta
from models.product import Product

class TrendDetector:
    def __init__(self, session):
        self.session = session

    def detect_emerging_trends(self, minimum_confidence=0.7):
        """Detect products showing early signs of trending"""
        emerging_trends = []
        
        # Get all products from the last 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        products = self.session.query(Product)\
            .filter(Product.timestamp >= thirty_days_ago)\
            .all()

        for product in products:
            trend_indicators = self._calculate_trend_indicators(product)
            
            # Calculate confidence score
            confidence_score = sum(trend_indicators.values()) / len(trend_indicators)
            
            if confidence_score >= minimum_confidence:
                emerging_trends.append({
                    'product': product,
                    'confidence': confidence_score,
                    'indicators': trend_indicators
                })

        return sorted(emerging_trends, key=lambda x: x['confidence'], reverse=True)

    def _calculate_trend_indicators(self, product):
        """Calculate various trend indicators"""
        return {
            'order_growth': self._check_order_growth(product),
            'review_velocity': self._check_review_velocity(product),
            'price_stability': self._check_price_stability(product),
            'social_mentions': self._check_social_mentions(product),
            'search_volume': self._check_search_volume(product)
        }

    def _check_order_growth(self, product):
        """Check if orders are consistently growing"""
        recent_orders = self._get_daily_orders(product, days=7)
        if len(recent_orders) < 7:
            return 0
        
        # Calculate day-over-day growth
        growth_rates = [
            (recent_orders[i] - recent_orders[i-1]) / recent_orders[i-1]
            for i in range(1, len(recent_orders))
            if recent_orders[i-1] > 0
        ]
        
        # Return percentage of positive growth days
        return sum(1 for rate in growth_rates if rate > 0) / len(growth_rates)

    def _get_daily_orders(self, product, days=7):
        """Get daily order counts for a product over the specified number of days"""
        # Calculate the start date
        start_date = datetime.now() - timedelta(days=days)
        
        # Query the database for orders in the date range
        daily_orders = self.session.query(Product)\
            .filter(Product.product_id == product.product_id)\
            .filter(Product.timestamp >= start_date)\
            .order_by(Product.timestamp.asc())\
            .all()
        
        # Return the order counts
        return [p.order_count for p in daily_orders]

    def _check_review_velocity(self, product):
        """Check the rate of new reviews"""
        start_date = datetime.now() - timedelta(days=7)
        
        # Get review counts for the last 7 days
        review_data = self.session.query(Product)\
            .filter(Product.product_id == product.product_id)\
            .filter(Product.timestamp >= start_date)\
            .order_by(Product.timestamp.asc())\
            .all()
        
        if len(review_data) < 2:
            return 0
        
        # Calculate review growth rate
        initial_reviews = review_data[0].review_count
        final_reviews = review_data[-1].review_count
        review_growth = (final_reviews - initial_reviews) / max(initial_reviews, 1)
        
        return min(max(review_growth, 0), 1)  # Normalize between 0 and 1

    def _check_price_stability(self, product):
        """Check if price is stable or following a positive trend"""
        start_date = datetime.now() - timedelta(days=7)
        
        price_data = self.session.query(Product)\
            .filter(Product.product_id == product.product_id)\
            .filter(Product.timestamp >= start_date)\
            .order_by(Product.timestamp.asc())\
            .all()
        
        if len(price_data) < 2:
            return 0
        
        # Calculate price volatility
        prices = [p.price for p in price_data]
        avg_price = sum(prices) / len(prices)
        volatility = sum(abs(p - avg_price) for p in prices) / len(prices) / avg_price
        
        return 1 - min(volatility, 1)  # Higher stability = lower volatility

    def _check_social_mentions(self, product):
        """Placeholder for social media mention tracking"""
        # This would typically integrate with social media APIs
        return 0.5  # Placeholder value

    def _check_search_volume(self, product):
        """Placeholder for search volume tracking"""
        # This would typically integrate with search analytics APIs
        return 0.5  # Placeholder value