class subjects:
    def __init__(self,name:str,final_grade:float,student_grade:float):
        self.name = name
        self.final_grade = final_grade
        self.student_grade = student_grade

class student:
    def __init__(self, name_: str, email: str):
        self.name = name_
        self.email = email
        self.gpa = []
        self.gpa_n = 0.0
        self.subjects = []

    def add_subject(self, subject):
        if not isinstance(subject, subjects):
            print("Error: subject must be an instance of Subject class")
        if subject.final_grade == 0:
            raise ValueError("final_grade cannot be 0")
        self.subjects.append(subject)   


    def calculate_gpa(self):
        for subject in self.subjects:
            if subject.student_grade / subject.final_grade >= 0.5:
                print(f"{self.name} passed with a GPA of {subject.name}")
                
            else:
                print(f"{self.name} failed with a GPA of {subject.name}")

def create_student():
    while True:
        try:
            name = str(input("Enter student name: "))
            break
        except ValueError:
            print("Error: name must be a string")

    while True:
        try:
            email = str(input("Enter student email: "))
            break
        except ValueError:
            print("Error: email must be a string")    

    student_info = student(name, email)
    return student_info

def create_subject():
   
    while True:
        name = input("Enter subject name: ")
        try:
            final_grade = float(input("Enter subject final grade: "))
            break
        except ValueError:
            print("Error: final grade must be a number")

    while True:
        try:
            student_grade = int(input("Enter student grade: "))
            break
        except ValueError:
            print("Error: student grade must be a number")

    subject_name = subjects(name, final_grade, student_grade)
    return subject_name



student1 = create_student()
subject1 = create_subject()
student1.add_subject(subject1)
subject2 = create_subject()
student1.add_subject(subject2)
student1.calculate_gpa()

student2 = create_student()
subject3 = create_subject()
student2.add_subject(subject3)
subject4 = create_subject()
student2.add_subject(subject4)
student2.calculate_gpa()