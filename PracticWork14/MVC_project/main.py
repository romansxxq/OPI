from model.OrderRepository import OrderRepository
from view.OrderView import OrderView
from controller.OrderController import OrderController

# Strategy
from model.priceCalculator import PriceCalculator
from model.concrete_strategies import NoDiscountStrategy, RegularCustomerStrategy, LargeOrderStrategy

# Observer
from model.order_service import OrderService
from observers.observers import LoggerObserver, StatisticsObserver

# Decorator
from decorators.base_service import BaseOrderService
from decorators.decorators import LoggingDecorator, TimingDecorator, AccessCheckDecorator

def run_mvc_demo():
    print("=== MVC Demo ===")
    repo = OrderRepository()
    view = OrderView()
    controller = OrderController(repo, view)
    controller.run()  # тут користувач може додавати замовлення, дивитися список та суму

def run_strategy_demo():
    print("\n=== Strategy Demo ===")
    calculator = PriceCalculator(NoDiscountStrategy())
    print("Без знижки:", calculator.calculate(100))
    calculator.set_strategy(RegularCustomerStrategy())
    print("Знижка постійного клієнта:", calculator.calculate(100))
    calculator.set_strategy(LargeOrderStrategy())
    print("Знижка для великого замовлення:", calculator.calculate(100))

def run_observer_demo():
    print("\n=== Observer Demo ===")
    service = OrderService()
    logger = LoggerObserver()
    stats = StatisticsObserver()
    service.subscribe(logger)
    service.subscribe(stats)

    service.create_order({'id': 1, 'amount': 100})
    service.create_order({'id': 2, 'amount': 200})

def run_decorator_demo():
    print("\n=== Decorator Demo ===")
    base_service = BaseOrderService()
    decorated_service = TimingDecorator(
                            LoggingDecorator(
                                AccessCheckDecorator(base_service, user_role="admin")
                            )
                        )
    decorated_service.execute()

if __name__ == "__main__":
    # запустимо по черзі всі демо
    run_mvc_demo()
    run_strategy_demo()
    run_observer_demo()
    run_decorator_demo()
