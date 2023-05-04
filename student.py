# class Student:
#     name = "Emily"
#     age = 20
#     school = "AkiraChix"
#     nationality = "Kenya"
class Student:
    school = "Akirachix"
    def __init__(self,age,school,nationality,first_name,last_name,country,name):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.name = name
        self.age = age
        self.school = school
        self.nationality=nationality
    def greet_Student(self):
        return f"Hello {self.name},welcome to {self.school},proudly {self.nationality}"  
    # question1
    def show_full_name(self):
        return f"Hello {self.first_name} {self.last_name}"
    def year_of_birth(self):
        return f"{2023-self.age}"
    def show_initials(self):
        return f"{self.first_name[0]},{self.last_name[0]}"
    

    
# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
