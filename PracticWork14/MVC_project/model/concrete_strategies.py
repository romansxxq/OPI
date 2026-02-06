from model.price_strategy import IPriceStrategy

class NoDiscountStrategy(IPriceStrategy):
    def calculate_price(self, price):
        return price

class RegularCustomerStrategy(IPriceStrategy):
    def calculate_price(self, price):
        return price * 0.9  # 10% discount

class LargeOrderStrategy(IPriceStrategy):
    def calculate_price(self, price):
        return price * 0.8  # 20% discount