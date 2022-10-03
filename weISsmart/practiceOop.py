#Write a short program that creates a student
#and a faculty member
#Get input for the first and last names of each
#Create a course
#Assign the course to the student
#For the student determine if they have a scholarship and store it
#>= 3.95 = full, > 3.9 = Part, Else None, when this method is called
#return the full name and a message about the scholarship status
#For the faculty, ask if they have tenure, return full name and tenure status
#In the course class, you have a name for the course. This is setup in the constructor

class Person :
    def __init__(self, Fname, Lname):
     self.first_name = Fname
     self.last_name = Lname 

class Student(Person):
    scholarship = ''
    
    def __init__(self, Fname, Lname, course, gpa):
        super().__init__(Fname, Lname)
        self.course = Course(course)
        self.gpa = gpa
        self.decide_scholarship()
    
    def decide_scholarship(self) :
        scholarship = ''
        if (self.gpa >= 3.95) :
            self.scholarship = 'Full'
        elif (self.gpa > 3.90) :
            self.scholarship = 'Part'
        else :
            self.scholarship = 'None'

        return

    def get_student_info(self) :
        return (str(self.first_name) + ' ' + str(self.last_name) + ' has the following scholarship: ' + str(self.scholarship))

class Faculty(Person) :
    def __init__(self, Fname, Lname, tenure) :
        super().__init__(Fname, Lname)
        self.tenure=tenure 

    def get_faculty_info(self) :
        if(self.tenure.upper() == "YES") :
            return (self.first_name + ' ' + self.last_name + ' has tenure.')
        else :
            return (self.first_name + ' ' + self.last_name + ' does not have tenure.')
class Course :
    def __init__(self, course_name) :
        self.course_name = course_name

    def get_course_name(self) :
        return self.course_name




student = Student(
    input('Enter student first name: '), 
    input('Enter student last name: '), 
    input('Enter course name: '), 
    float(input('Enter gpa: '))
    )

faculty = Faculty(
    input('Enter faculty first name: '), 
    input('Enter faculty last name: '), 
    input('Does this faculty member have tenure? ').upper()
    )

print(student.get_student_info())
print(faculty.get_faculty_info())
