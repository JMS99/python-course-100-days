student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def dertermine_grades():
    student_grades.update(student_scores)
    print(student_grades)
    for key, value in student_grades.items():
        if value <= 100 and value >= 91:
            new_values = {key: "Outstanding"}
        elif value <= 90 and value >= 81:
            new_values = {key: "Exceeds Expectations"}
        elif value <=80 and value >=71:
            new_values = {key: "Acceptable"}
        else:
            new_values = {key: "Fail"}
        student_grades.update(new_values)
    print(student_grades)
    
dertermine_grades()