class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, Score: {self.score})"


# Creating three student objects
student1 = Student(1, "Justin", 85)
student2 = Student(2, "Alex", 90)
student3 = Student(3, "Max", 78)

# Storing them in a list
students = [student1, student2, student3]

# Printing the list
for student in students:
    print(student)