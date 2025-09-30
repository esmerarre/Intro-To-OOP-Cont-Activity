from school_schedule.student import Student

# Write your tests here!
def test_students_initialization():
    #Arrange
    name = "Xin"
    grade = "Senior"
    classes = ["Chemistry"]

    #Act
    student = Student(name, grade, classes)

    #Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes


def test_check_num_classes():
     #Arrange
    name = "Xin"
    grade = "Senior"
    classes = [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
    student = Student(name, grade, classes)

    #Act
    result = student.get_num_classes()

    #Assert
    assert result == 6
    assert student.classes == classes

def test_check_num_classes_empty():
     #Arrange
    name = "Xin"
    grade = "Senior"
    classes = []
    student = Student(name, grade, classes)

    #Act
    result = student.get_num_classes()

    #Assert
    assert result == 0
    assert student.classes == classes




    