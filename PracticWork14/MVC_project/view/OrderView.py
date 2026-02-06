class OrderView:
    def show_menu(self):
        print("1. Створити замовлення")
        print("2. Переглянути замовлення")
        print("3. Переглянути загальну суму замовлень")
        print("4. Вийти")

    def read_int(self):
        return int(input("Ваш вибір: "))
    
    def read_float(self):
        return float(input("Введіть суму замовлення: "))
    
    def show_orders(self, orders):
        if not orders:
            print("Немає замовлень.")
        else:
            for order in orders:
                print(f"Замовлення ID: {order.order_id}, Сума: {order.amount}")
    
    def show_total_amount(self, total):
        print(f"Загальна сума замовлень: {total}")