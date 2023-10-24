class Students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def wanafunzi(self):
        print("Name: %s \nCourse: %s \nGender: %s \n Age: %d"
               % (self.name, self.course, self.gender, self.age))

Student1 = Students("Erick Were", "Computer Science", "Male",85)
Student1.wanafunzi()
student2 =Students("Anne Thumbi", "Engineering", "Female", 20)
Student1.wanafunzi()
Student3 = Students("James Kinoti", "Cybersecurity", "male" ,35)
Student3.wanafunzi()
Students4 = Students( "Veronicah Henry", "Telecommunications ", "female",21)