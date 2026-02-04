# Task 1
list = [5, 3, 8, 6, 2, 7, 4, 1, 9, 0]

def findMinMax(lst):
    minmum = lst[0]
    maximum = lst[0]
    for number in lst:
        if number < minmum:
            minmum = number
        if number > maximum:
            maximum = number
    return minmum, maximum

def CalculateSum(lst):
    total = 0
    for number in lst:
        total += number
    return total

def CalculateAverage(lst):
    total = CalculateSum(lst)
    average = total / len(lst)
    return average

min_value, max_value = findMinMax(list)
sum_value = CalculateSum(list)
average_value = CalculateAverage(list)
print("List:", list)
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Sum: {sum_value}")
print(f"Average: {average_value}")

# Task 2
data = [[1,4,7],[2,5],[9,3,6,8]]

def flattenList(nested_lst):
    result = []
    for innerList in nested_lst:
        for num in innerList:
            result.append(num)
    return result

def SortList(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

flat_list = flattenList(data)
sorted_list = SortList(flat_list)
print("Original nested list:", data)
print("Flattened list:", flat_list)
print("Sorted list:", sorted_list)

# Task 3

students = [
    ("Іван", 85),
    ("Марія", 92),
    ("Олег", 78),
    ("Анна", 90)
]
def findTopStudent(students_lst):
    top_student = students_lst[0]
    for student in students_lst:
        if student[1] > top_student[1]:
            top_student = student
    return top_student

top_student = findTopStudent(students)
print("Students:", students)
print(f"Top student: {top_student[0]} with score {top_student[1]}")

def getMarks(students_lst):
    marks = []
    for student in students_lst:
        marks.append(student[1])
    return marks
marks_list = getMarks(students)
print("Marks list:", marks_list)

def StudentsWithHighMarks(students_lst, given_mark):
    count = 0
    high_mark_students = []
    for student in students_lst:
        if student[1] > given_mark:
            count += 1
            high_mark_students.append(student)
    return count, high_mark_students
count, high_mark_students = StudentsWithHighMarks(students, 80)
print ("Number of students with marks greater than 80:", count)
print("Students with marks greater than 80:", high_mark_students)