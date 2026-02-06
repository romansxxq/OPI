class PriceCalculator:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy
        
    def calculate_price(self, price):
        return self._strategy.calculate_price(price)