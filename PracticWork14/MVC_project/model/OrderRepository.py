class OrderRepository:
    def __init__(self):
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def get_all(self):
        return self._orders
    
    def get_total_amount(self):
        return sum(order.amount for order in self._orders)