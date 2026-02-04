# Stack

# stack = []

# stack.append(50)
# stack.append(100)
# stack.append(150)
# stack.append(200)
# stack.append(250)

# print("Initial stack:", stack)

# # Pop elements from the stack
# stack.pop()
# stack.pop()
# print("Stack after popping two elements:", stack)

# def is_empty(stack):
#     return len(stack) == 0
# print("Is the stack empty?", is_empty(stack))

# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else: return None
# print("Top element of the stack:", peek(stack))

# def reverseStack(s):
#     stack1 = []

#     for char in s:
#         stack1.append(char)
    
#     reversed_str = ""
#     while not is_empty(stack1):
#         reversed_str += stack1.pop()
    
#     return reversed_str

# user_input = input("Enter a string to reverse: ")
# reversed_string = reverseStack(user_input)
# print("Reversed string:", reversed_string)

# Queue

from collections import deque

# deque = deque()

# deque.append(10)
# deque.append(20)
# deque.append(30)
# deque.append(40)
# deque.append(50)
# print("Initial queue:", deque)
# deque.popleft()
# deque.popleft()
# deque.popleft()
# print("Queue after dequeuing three elements:", deque)

# customers = deque()

# def add_customer(queue, name):
#     queue.append(name)
#     print(f"Customer {name} added to the queue.")

# def serve_customer(queue):
#     if len(queue) > 0:
#         serverd = queue.popleft()
#         print(f"Customer {serverd} has been served.")
#     else:
#         print("No customers in the queue.")

# def show_queue(queue):
#     if len(queue) > 0:
#         print("Current queue:", list(queue))
#     else:
#         print("The queue is empty.")

# add_customer(customers, "Alice")
# add_customer(customers, "Bob")
# add_customer(customers, "Charlie")

# show_queue(customers)

# serve_customer(customers)
# show_queue(customers)

# add_customer(customers, "Diana")
# show_queue(customers)

# Dictionary

# students = {
#     "name": "Roman", 
#     "age": 19,
#     "group": "IPZ-3/2",
# }
# print(students)

# students["course"] = 3
# print(students)

# students["age"] = 20
# print(students)

# del students["group"]
# print(students)

# print("Keys:", list(students.keys()))
# print("Values:", list(students.values()))

# marks = [5,4,5,3,4,5,3]
# marks_count = {
#     5: 0,
#     4: 0,
#     3: 0,
# }
# for mark in marks:
#     if mark in marks_count:
#         marks_count[mark] += 1
# print("Marks count:", marks_count)
def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    products[name] = price
    print(f"Product {name} added with price {price}.")
    return products
def delete_product(products):
    name = input("Enter product name to delete: ")
    if name in products:
        del products[name]
        print(f"Product {name} deleted.")
    else:
        print(f"Product {name} not found.")
    return products
def show_products(products):
    if products:
        print("Products:")
        for name, price in products.items():
            print(f"- {name}: {price}")
    else:
        print("No products available.")

def main_menu():
    products = {}
    while True:
        print("Main Menu:")
        print("1. Додати товар")
        print("2. Видалити тоівар")
        print("3. Показати всі товари")
        print("0. Вийти")

        choice = int(input("Enter your choice (1-3): "))
        if choice == 1: products = add_product(products)
        elif choice == 2: products = delete_product(products)
        elif choice == 3: show_products(products)
        elif choice == 0: break
        else:
            print("Invalid choice. Please try again.")
            return main_menu()
    
    
if __name__ == "__main__":
    main_menu()