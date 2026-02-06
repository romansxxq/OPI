class OrderController:
    def __init__(self, order_repository, view):
        self.order_repository = order_repository
        self.view = view
        self.next_order_id = 1

    def add_order(self, order):
        self.order_repository.add_order(order)

    def display_orders(self):
        orders = self.order_repository.get_all()
        self.view.show_orders(orders)

    def display_total(self):
        total = self.order_repository.get_total_amount()
        self.view.show_total_amount(total)

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.read_int()

            if choice == 1:
                amount = self.view.read_float()
                # create order using controller's counter
                from Model.Order import Order

                order = Order(self.next_order_id, amount)
                self.add_order(order)
                self.next_order_id += 1
            elif choice == 2:
                self.display_orders()
            elif choice == 3:
                self.display_total()
            elif choice == 4:
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")