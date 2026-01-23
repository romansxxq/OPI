# Функція для обчислення суми елементів множини
def SumOfSet(unique_numbers):
    total = 0
    for number in unique_numbers:
        total += number
    return total

# Функція для перевірки наявності числа в множині
def CheckNumberInSet(unique_set, number):
    found = False
    for num in unique_set:
        if num == number:
            found = True
            break
    
    if found:
        print(f"The number {number} is present in the set.")
    else:
        print(f"The number {number} is not present in the set.")

def main():
    #Введення послідовності цілих чисел
    input_numbers = input("Enter a sequence of integers separated by spaces: ")
    numbers_list = list(map(int, input_numbers.split()))

    #Формування множини унікальних чисел
    numbers_set = set(numbers_list)
    print(f"Unique numbers: {numbers_set}")

    #Введення заданого числа
    x = int(input("Enter number x: "))

    count = 0
    for number in numbers_set:
        if number > x:
            count += 1

    print(f"Count of unique numbers greater than {x}: {count}")

    resultSum = SumOfSet(numbers_set)
    print(f"Sum of unique numbers: {resultSum}")

    # Перевірка належності числа множині
    check_value = int(input("Введіть число для перевірки належності множині: "))
    CheckNumberInSet(numbers_set, check_value)

if __name__ == "__main__":
    main()